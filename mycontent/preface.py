# %% [markdown]
# <title>Learn Quantum Computation using Qiskit</title>
# <div class="preface-top">
#     <div class="preface-checker-pattern"></div>
# <div class="preface-summary">
#   <aside class="preface-summary-image"><img src="images/preface_illustration_2.svg"></aside>
#   <div class="preface-summary-text">
#      <p>
#       Greetings from the Qiskit Community team! This textbook is a university quantum algorithms/computation course supplement based on Qiskit to help learn:</p>
#       <ol>
#           <li>The mathematics behind quantum algorithms</li>
#           <li>Details about today's non-fault-tolerant quantum devices</li>
#           <li>Writing code in Qiskit to implement quantum algorithms on IBM's cloud quantum systems</li>
#       </ol>
# </div>
#     <a href="https://qiskit.org/textbook/ch-states/introduction.html"><button class="preface-button read-textbook">Read the textbook <span class="rangle"><img src="/textbook/assets/images/rightarrow.svg"></span></button></a>
# </div>

# %% [markdown]
# # About the Textbook
#
# <p>This is a free digital textbook that will teach you the concepts of quantum computing while you learn to use the Qiskit SDK.</p>
#
# ## Run the Code Inline
#
# <p>This textbook is built on a jupyter notebook framework that allows for easy reading, but it also allows readers to edit and run the code right in the textbook. The chapters can also be opened as Jupyter notebooks in the <a href="https://quantum-computing.ibm.com/jupyter">IBM Quantum Experience</a>, no installs required!</p>

# %%
# Click 'try', then 'run' to see the output,
# you can change the code and run it again.
print("This code works!")
from qiskit import QuantumCircuit
qc = QuantumCircuit(2) # Create circuit with 2 qubits
qc.h(0)    # Do H-gate on q0
qc.cx(0,1) # Do CNOT on q1 controlled by q0
qc.measure_all()
qc.draw()

# %% [markdown]
# <a href="https://qiskit.org/textbook/widgets-index.html"><button class="preface-button">Interactivity Tour<span class="rangle"><img src="/textbook/assets/images/rightarrow.svg"></span></button></a>
#
# ## Learn with Real Quantum Systems
#
# <p>The best way to learn is by doing. Qiskit allows users to run experiments on state-of-the-art quantum devices from the comfort of their homes. The textbook teaches not only theoretical quantum computing, but the experimental quantum physics that realises it.</p>
#
# <img src="images/preface-hw-example.png" class="preface-image">
#
# <a href="https://qiskit.org/textbook/ch-quantum-hardware/accessing_higher_energy_states.html"><button class="preface-button">See Example: Accessing Higher Level States<span class="rangle"><img src="/textbook/assets/images/rightarrow.svg"></span></button></a>
#
# # Using the Textbook
#
# <p>If you're reading the textbook independently, you don't have to read it all in order, but we recommend you read chapters 1-3 first.</p>
#
# ## Curriculum Integration
#
# <p>The textbook can be followed as an independent course, however it has been designed to accompany a traditional university course. The textbook shows students how to use Qiskit to experiment with quantum algorithms and hardware, and uses this to reinforce their understanding.
# </p>
#
# <img src="images/curriculum.svg" class="preface-image">
#
# ## Use the Textbook in Your Course
#
# If you are using the Qiskit Textbook in your course, you can join the IBM Quantum Educators Program. The Program provides:
#
# <ul class="preface-list">
# <li> The ability to reserve time for priority access to our open systems for in-class demonstrations </li>
# <li> Access to additional premium systems beyond our open systems</li>
# <li> Access to a 5-qubit system with full microwave control using Qiskit Pulse</li>
# </ul>
#     
# <a href="https://quantum-computing.ibm.com/programs/educators"><button class="preface-button">Sign Up for the IBM Quantum Educators Program<span class="rangle"><img src="/textbook/assets/images/rightarrow.svg"></span></button></a>
#
# #  Contact
#
# <p> If you have any questions or suggestions about the textbook or would like to incorporate it into your curriculum, please contact Frank Harkins <a href="mailto:Francis.Harkins@ibm.com">(Francis.Harkins@ibm.com)</a>. In the true spirit of open-source, any chapter contributions are welcome in this GitHub repository.</p>
#     
# # Contributors
#
# <p> Learn Quantum Computation using Qiskit is the work of several individuals. If you use it in your work, cite it using <a href="https://github.com/qiskit-community/qiskit-textbook/blob/master/content/qiskit-textbook.bib">this bib file</a> or directly as:</p>
# <p><i>
# Abraham Asfaw, Luciano Bello, Yael Ben-Haim, Sergey Bravyi, Lauren Capelluto, Almudena Carrera Vazquez, Jack Ceroni, Richard Chen, Albert Frisch, Jay Gambetta, Shelly Garion, Leron Gil, Salvador De La Puente Gonzalez, Francis Harkins, Takashi Imamichi, David McKay, Antonio Mezzacapo, Zlatko Minev, Ramis Movassagh, Giacomo Nannicni, Paul Nation, Anna Phan, Marco Pistoia, Arthur Rattew, Joachim Schaefer, Javad Shabani, John Smolin, Kristan Temme, Madeleine Tod, Stephen Wood, James Wootton.</i></p>

# %%
