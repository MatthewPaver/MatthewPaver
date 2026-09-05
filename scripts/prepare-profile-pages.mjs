// This profile repository is not a second portfolio. Preserve old HTML entry
// points as redirects without publishing the retired catalogue or its assets.
import fs from 'node:fs';
import path from 'node:path';

const output = 'profile-pages';
const redirect = fs.readFileSync('index.html', 'utf8');
fs.rmSync(output, { recursive: true, force: true });
fs.mkdirSync(output, { recursive: true });
fs.writeFileSync(path.join(output, 'index.html'), redirect);
fs.copyFileSync('CV.pdf', path.join(output, 'CV.pdf'));

function preserveHtmlRoutes(directory) {
  if (!fs.existsSync(directory)) return;
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const source = path.join(directory, entry.name);
    if (entry.isDirectory()) preserveHtmlRoutes(source);
    else if (entry.isFile() && entry.name.endsWith('.html')) {
      const destination = path.join(output, source);
      fs.mkdirSync(path.dirname(destination), { recursive: true });
      fs.writeFileSync(destination, redirect);
    }
  }
}

preserveHtmlRoutes('store');
console.log('Prepared profile redirects and CV. The portfolio lives at matthewpaver.github.io.');
