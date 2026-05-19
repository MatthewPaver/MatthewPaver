# What a 167-test scraping suite actually catches

> Matthew Paver · May 2026 · ~5 minute read

I run a venue ingestion pipeline called Happening. It pulls events from 103 different London venues. Different CMS systems, different markup, different ways of telling you when a band is playing. The reliability suite is 167 tests. Most of them have nothing to do with the happy path.

When people see the test count they assume it's overkill. It isn't. Here's what the tests actually catch, and what the happy-path version of this codebase would miss.

## 1. Dates that aren't dates

The most common failure is a venue saying "Tonight". Their CMS knows what tonight means. My scraper does not, unless I tell it. "Sat 14th" with no year is another. "From 8pm" with no end time. "Doors 7, show 8". One venue lists doors-open three different ways on the same page depending on which template the editor reached for.

I have 23 tests for date parsing. They look boring. They cover specific strings I have seen break the parser in production. Every time something new breaks I add the string as a test and fix the parser. The tests aren't aspirational. They're a graveyard.

## 2. The site is up, but the page is wrong

A scraper that only checks for HTTP 200 will happily ingest a coming-soon page, a cookie wall, a JS-rendered shell with no real content, or a "we're under maintenance" placeholder that returns 200 because the CMS treats it as a perfectly valid response.

I have tests that assert at least one event exists in the parsed output, and tests that flag suspiciously low counts compared to the last successful run. A venue that normally returns 40 events shouldn't suddenly return 2 without me noticing. The tests catch the silent failures: the ones where everything looks fine and the data is wrong.

## 3. The same gig under three names

Cross-venue dedupe is where naive scrapers fall apart. The same gig gets listed by the venue, the promoter, and a ticket aggregator. Three sources, three slightly different titles, three slightly different start times because someone rounded. My dedupe is fuzzy on purpose, which means I need tests that prove it isn't too fuzzy.

The dedupe tests pin known overlaps: real events from previous months where I went back and confirmed which listings were duplicates. If the fuzzy logic drifts, the test fails. If I tighten it too much, a different test fails because actual duplicates start appearing again. The tests are pulling in two directions at once. That's the point.

## 4. The venue changed their HTML

Layout drift is the failure mode every scraper hits eventually. A class gets renamed. A `<div>` becomes a `<section>`. The selector breaks silently and the scraper returns zero events without raising anything.

I have a check per venue that asserts a minimum event count under normal conditions. If a venue's count goes to zero, the deployment fails before anything reaches production. The test isn't elegant. It's a tripwire.

## 5. The data is right but the encoding is wrong

A venue using a smart-quote in an event title will break naive JSON serialisation if UTF-8 isn't set somewhere upstream. Apostrophes from Word documents are different characters to apostrophes from a phone keyboard. One French restaurant lists its venue name in three different encodings depending on which page you scrape.

I have tests that round-trip non-ASCII characters end to end: through the parser, the dedupe layer, the database write, and the output file. Two of those tests exist because a deploy went out with `Caf?` instead of `Café` and nobody noticed for a day.

## 6. The clock is lying

Timezones are the bug you don't see until daylight savings. London time is UTC most of the year and UTC+1 from late March to late October. A scraper that reads "8pm" without a timezone marker can be silently an hour off for half the year.

I have tests that fix the system clock to specific moments: the day before the spring transition, the day after, the autumn transition both directions. They catch the kind of off-by-one-hour errors that show up as "this gig is at 7pm but the website says 8pm" complaints from users.

## What this is really about

A 167-test suite isn't impressive on its own. The number doesn't mean anything by itself. What it means is that 167 specific things have gone wrong, or could go wrong, and I've written down the shape of the failure so future-me has to argue with the test before shipping a regression.

The opinion I'll defend: scraping isn't an exercise in CSS selectors. The selector is the easy part. The hard part is failure modes. The silent ones. The timezone ones. The encoding ones. The ones that only happen at 02:00 on the last Sunday of October. Tests are how I make those failures loud.

When I show this work to people, they sometimes ask why it isn't an LLM doing the scraping. That's a separate post. The short version: an LLM can guess the start time. A test suite can tell you when it's wrong.

— Matthew
