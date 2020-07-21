![image](resources/qgss-header.png)


# Lab 1: Single-qubit and multi-qubit states, quantum teleportation


In this lab, you will learn how to write `Qiskit` code and investigate single-qubit and multi-qubit states using the `qpshere` visualization that you learned in lecture 1.

If you have not used Jupyter notebooks before, take a look at the following video to quickly get started.
- https://www.youtube.com/watch?v=jZ952vChhuI

Remember, to run a cell in Jupyter notebooks, you press `Shift` + `Return/Enter` on your keyboard.


### Installing necessary packages


Before we begin, you will need to install some prerequisites into your environment. Run the cell below to complete these installations. At the end, the cell outputs will be cleared.

```python
# !pip install -U -r grading_tools/requirements.txt

from IPython.display import clear_output
clear_output()
```

# Single-qubit states


In lecture, you learned that single qubit states can be written down generally as 

$$\sqrt{1-p}\vert0\rangle + e^{i\phi}\sqrt{p}\vert1\rangle$$

Here, $p$ is the probability that a measurement of the state in the computational basis $\{\vert0\rangle, \vert1\rangle\}$ will have the outcome $1$, and $\phi$ is the phase between the two computational basis states. 

Single-qubit gates can then be used to manipulate this quantum state by changing either $p$, $\phi$, or both.

Let's begin by creating a single-qubit quantum circuit. We can do this in `Qiskit` using the following:

```python
from qiskit import QuantumCircuit

mycircuit = QuantumCircuit(1)
mycircuit.draw('mpl')
```

The above quantum circuit does not contain any gates. Therefore, if you start in any state, say $\vert0\rangle$, applying this circuit to your state doesn't change the state. 

To see this clearly, let's create the statevector $\vert0\rangle$. In `Qiskit`, you can do this using the following:

```python
from qiskit.quantum_info import Statevector

sv = Statevector.from_label('0')
```

You can see what's contained in the object `sv`:

```python
sv
```

The vector itself can be found by writing

```python
sv.data
```

As you can see, the above matches what you learned in lecture. Recall that $$\vert0\rangle = \begin{bmatrix}1\\0\end{bmatrix}$$

We can now apply the quantum circuit `mycircuit` to this state by using the following:

```python
new_sv = sv.evolve(mycircuit)
```

Once again, you can look at the new statevector by writing

```python
new_sv
```

As you can see, the statevector hasn't changed. Recall the concept of state projection that you learned in lecture. You can compute the projection of `new_sv` onto `sv` by writing

```python
from qiskit.quantum_info import state_fidelity

state_fidelity(sv, new_sv)
```

As you can see, the projection of `new_sv` onto `sv` is 1, indicating that the two states are identical. You can visualize this state using the `qsphere` by writing

```python
from qiskit.visualization import plot_state_qsphere

plot_state_qsphere(sv.data)
```

As you learned in lecture 1, applying an $X$ gate flips the qubit from the state $\vert0\rangle$ to the state $\vert1\rangle$. To see this clearly, we will first create a single-qubit quantum circuit with the $X$ gate.

```python
mycircuit = QuantumCircuit(1)
mycircuit.x(0)

mycircuit.draw('mpl')
```

Now, we can apply this circuit onto our state by writing

```python
sv = Statevector.from_label('0')
new_sv = sv.evolve(mycircuit)
new_sv
```

As you can see, the statevector now corresponds to that of the state $\vert1\rangle$. Recall that

$$\vert1\rangle = \begin{bmatrix}0\\1\end{bmatrix}$$


Now, the projection of `new_sv` onto `sv` is 

```python
state_fidelity(new_sv, sv)
```

This is not surprising. Recall from the lecture that the states $\vert0\rangle$ and $\vert1\rangle$ are orthogonal. Therefore, $\langle0\vert1\rangle = 0$. The state can be shown on the `qsphere` by writing

```python
plot_state_qsphere(new_sv.data)
```

Similarly, we can create the state $$\frac{1}{\sqrt{2}}\left(\vert0\rangle + \vert1\rangle\right)$$
by applying a Hadamard gate as you learned in lecture. Here is how we can create the state and visualize it in `Qiskit`:

```python
sv = Statevector.from_label('0')
mycircuit = QuantumCircuit(1)
mycircuit.h(0)
mycircuit.draw('mpl')
```

```python
new_sv = sv.evolve(mycircuit)
print(new_sv)
plot_state_qsphere(new_sv.data)
```

As you can see above, the state has equal components of $\vert0\rangle$ and $\vert1\rangle$. The size of the circle is proportional to the probability of measuring each basis state in the statevector. As a result, you can see that the size of the circles is half of the size of the circles in our previous visualizations.


Recall from lecture that we can also create other superpositions with different phase. Let's create $$\frac{1}{\sqrt{2}}\left(\vert0\rangle - \vert1\rangle\right)$$ which can be done by applying the Hadamard gate on the state $\vert1\rangle$.

```python
sv = Statevector.from_label('1')
mycircuit = QuantumCircuit(1)
mycircuit.h(0)

new_sv = sv.evolve(mycircuit)
print(new_sv)
plot_state_qsphere(new_sv.data)
```

This time, the bottom circle, corresponding to the basis state $\vert1\rangle$ has a different color corresponding to the phase of $\phi = \pi$. This is because the coefficient of $\vert1\rangle$ in the state $$\frac{1}{\sqrt{2}}\left(\vert0\rangle - \vert1\rangle\right)$$ is $-1$, which is equal to $e^{i\pi}$.

Other phases can also be created by applying different gates. The $T$ and $S$ gates apply phases of $+\pi/4$ and $+\pi/2$, respectively. The widget below helps you see different gates, and their actions on single-qubit quantum states.

```python
from resources.qiskit_textbook.widgets import gate_demo
gate_demo(qsphere=True)
```

A summary of the operations of the most common gates on single-qubit states is given by the handy image below, where the phases are shown in degrees.

![image](resources/gates-and-qspheres.png)


# Multi-qubit states


Similar to the discussion above, you can also explore multi-qubit gates in `Qiskit`. In lecture, you learned about Bell states, and how they can be generated using quantum gates. We will demonstrate below how to create the Bell state $$\frac{1}{\sqrt{2}}\left(\vert00\rangle + \vert11\rangle\right)$$ from the state $\vert00\rangle$. We'll start by visualizing the state $\vert00\rangle$ using the same procedure:

```python
sv = Statevector.from_label('00')
plot_state_qsphere(sv.data)
```

Next, we use the Hadamard gate described above, along with a controlled-X gate, to create the Bell state.

```python
mycircuit = QuantumCircuit(2)
mycircuit.h(0)
mycircuit.cx(0,1)
mycircuit.draw('mpl')
```

The result of this quantum circuit on the state $\vert00\rangle$ is found by writing

```python
new_sv = sv.evolve(mycircuit)
print(new_sv)
plot_state_qsphere(new_sv.data)
```

Note how this looks very similar to a single-qubit superposition with zero phase. Following entanglement, it is no longer possible to treat the two qubits individually, and they must be considered to be one system. 

To see this clearly, we can see what would happen if we measured the Bell state above 1000 times.

```python
counts = new_sv.sample_counts(shots=1000)

from qiskit.visualization import plot_histogram
plot_histogram(counts)
```

As you can see above, all measurements give either the result `00` or `11`. In other words, if the measurement outcome for one of the qubits is known, then the outcome for the other is fully determined.


### Ungraded exercise 1

Can you create the state $$\frac{1}{\sqrt{2}}\left(\vert01\rangle + \vert10\rangle\right)$$ using a similar procedure?


### Ungraded exercise 2

Can you create the state $$\frac{1}{\sqrt{2}}\left(\vert01\rangle - \vert10\rangle\right)$$ using a similar procedure?


# Measurements


In the above example, we simulated the action of a measurement by sampling counts from the statevector. A measurement can explicitly be inserted into a quantum circuit as well. Here is an example that creates the same Bell state and applies a measurement.

```python
mycircuit = QuantumCircuit(2, 2)
mycircuit.h(0)
mycircuit.cx(0,1)
mycircuit.measure([0,1], [0,1])
mycircuit.draw('mpl')
# mycircuit.draw()
```

Two new features appeared in the circuit compared to our previous examples. 

- First, note that we used a second argument in the `QuantumCircuit(2,2)` command. The second argument says that we will be creating a quantum circuit that contains two qubits (the first argument), and two classical bits (the second argument).
- Second, note that the `measure` command takes two arguments. The first argument is the set of qubits that will be measured. The second is the set of classical bits onto which the outcomes from the measurements of the qubits will be stored.


Since the above quantum circuit contains non-unitaries (the measurement gates), we will use `Qiskit`'s built-in `Aer` simulators to run the circuit. To get the measurement counts, we can use the following code:

```python
from qiskit import Aer, execute
simulator = Aer.get_backend('qasm_simulator')
result = execute(mycircuit, simulator, shots=10000).result()
counts = result.get_counts(mycircuit)
plot_histogram(counts)
```

As you can see, the measurement outcomes are similar to when we sampled counts from the statevector itself.


# Graded exercise 1: Quantum teleportation


In this graded exercise, you will teleport the quantum state 
$$\sqrt{0.70}\vert0\rangle + \sqrt{0.30}\vert1\rangle$$ from Alice's qubit to Bob's qubit. Recall that the teleportation algorithm consists of four major components:

1. Initializing the state to be teleported. We will do this on Alice's qubit `q0`.
2. Creating entanglement between two qubits. We will use qubits `q1` and `q2` for this. Recall that Alice owns `q1`, and Bob owns `q2`.
3. Applying a Bell measurement on Alice's qubits `q0` and `q1`.
4. Applying classically controlled operations on Bob's qubit `q2` depending on the outcomes of the Bell measurement on Alice's qubits.

This exercise guides you through each of these steps.


### Initializing the state to be teleported


First, create a quantum circuit that creates the state $$\sqrt{0.70}\vert0\rangle + \sqrt{0.30}\vert1\rangle$$ You can do this by using `Qiskit`'s `initialize` function.

```python
def initialize_qubit(given_circuit, qubit_index):
    
    import numpy as np
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    mycircuit = QuantumCircuit(2, 2)
    mycircuit.h(0)
    mycircuit.cx(0,1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    
    return given_circuit
```

Next, we need to create entanglement between Alice's and Bob's qubits.

```python
def entangle_qubits(given_circuit, qubit_Alice, qubit_Bob):
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    
    return given_circuit
```

Next, we need to do a Bell measurement of Alice's qubits.

```python
def bell_meas_Alice_qubits(given_circuit, qubit1_Alice, qubit2_Alice, clbit1_Alice, clbit2_Alice):
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    

    ### WRITE YOUR CODE BETWEEN THESE LINES - END

    
    return given_circuit
```

Finally, we apply controlled operations on Bob's qubit. Recall that the controlled operations are applied in this order:

- an $X$ gate is applied on Bob's qubit if the measurement coutcome of Alice's second qubit, `clbit2_Alice`, is `1`.
- a $Z$ gate is applied on Bob's qubit if the measurement coutcome of Alice's first qubit, `clbit1_Alice`, is `1`.

```python
def controlled_ops_Bob_qubit(given_circuit, qubit_Bob, clbit1_Alice, clbit2_Alice):
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    
    return given_circuit
```

The next lines of code put everything together. **You do not need to modify anything below, but you will need to run the cell to submit your solution.**

```python
### imports
from qiskit import QuantumRegister, ClassicalRegister

### set up the qubits and classical bits
all_qubits_Alice = QuantumRegister(2)
all_qubits_Bob = QuantumRegister(1)
creg1_Alice = ClassicalRegister(1)
creg2_Alice = ClassicalRegister(1)

### quantum teleportation circuit here
# Initialize
mycircuit = QuantumCircuit(all_qubits_Alice, all_qubits_Bob, creg1_Alice, creg2_Alice)
initialize_qubit(mycircuit, 0)
mycircuit.barrier()
# Entangle
entangle_qubits(mycircuit, 1, 2)
mycircuit.barrier()
# Do a Bell measurement
bell_meas_Alice_qubits(mycircuit, all_qubits_Alice[0], all_qubits_Alice[1], creg1_Alice, creg2_Alice)
mycircuit.barrier()
# Apply classically controlled quantum gates
controlled_ops_Bob_qubit(mycircuit, all_qubits_Bob[0], creg1_Alice, creg2_Alice)

### Look at the complete circuit
print(mycircuit.draw(output='text'))

### store the circuit as the submitted answer
answer = mycircuit
```

Then, grade your solution by running the cell below. Provide always the same name and email, as the one you wrote during the course sign up.

```python
name = 'First Last'
email = 'first.last@domain.com'

from grading_tools import grade
grade(answer, name, email, 'lab1', 'ex1')
```

# Additional reading

- You can watch a video on building the quantum teleportation quantum circuit here: https://www.youtube.com/watch?v=mMwovHK2NrE&list=PLOFEBzvs-Vvp2xg9-POLJhQwtVktlYGbY&index=6&t=0s

- For additional details about the quantum teleportation algorithm, including the principle of deferred measurement, you can refer to the Qiskit Textbook's section on the algorithm here: https://qiskit.org/textbook/ch-algorithms/teleportation.html

- The `1 minute Qiskit` episode entitled `What is the qsphere?` succinctly describes the Qsphere visualization tool that we used in this lab. You can find it here: https://youtu.be/4SoK2h4a7us
