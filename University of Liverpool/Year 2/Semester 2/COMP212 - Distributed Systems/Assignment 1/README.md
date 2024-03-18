## Instructions for Compiling and Running the Leader Election Algorithm

### 3.1 Asynchronous-Start and Terminating LCR Algorithm

To compile and run the LCR algorithm for a ring network:

1. **Navigate** to the `3.1` folder containing `Processor.java`, `Ring.java`, and `Main.java`.
2. **Compile** the Java files using the commands: `javac Processor.java`, `javac Ring.java`, and `javac Main.java`.
3. 3. Run the `Main` class with the command: `Main.java`


This will start the leader election process in the ring network and output the elected leader's ID.

---

### 3.2 Leader-Election Algorithm for Rings of Rings

To compile and run the leader election for a ring of rings network:

1. Ensure `Processor.java`, `Ring.java`, `InterfaceProcessor.java`, `RingOfRings.java`, and `Main.java` are in the `3.2` folder.
2. Compile the files with the commands:  `javac Processor.java`, `javac Ring.java`, and `javac InterfaceProcessor.java`, `javac RingOfRings.java`. `javac Main.java`.
3. Run the `Main` class with the command: `Main.java`

This will execute the leader election in the ring of rings network and print the results.

---

### 3.3 Experimental Evaluation & Report

To execute the algorithm in networks of varying size and structure and log the results:

1. **Navigate** to the `3.2` folder.
2. Compile the files with the commands:`javac Processor.java`, `javac Ring.java`, and `javac InterfaceProcessor.java`, `javac RingOfRings.java`.
`javac ExperimentLogger.java`. `javac Simulator.java`.
3. Run the `Simulator` class with the command: `Simulator.java`
This will perform the experiments and log the data to `experiment_log.csv`.

To view the **Experimental Evaluation - Section 3.3**, it is in the root folder of when you first open `Assignment 1`.

---

### To Generate the Plots with the Logged Data

1. Ensure Python is installed along with matplotlib and pandas libraries.
2. Open `Visualisations.py` in a Python IDE or text editor. This is saved the `3.2` folder.
3. Run the Python script to generate the plots: `python Visualisations.py`.

