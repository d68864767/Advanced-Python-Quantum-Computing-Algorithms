# quantum_algorithms.py

# Importing required libraries
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Function to create Bell State
def create_bell_state():
    circuit = QuantumCircuit(2)
    # Apply Hadamard gate on the first qubit
    circuit.h(0)
    # Apply CNOT gate
    circuit.cx(0, 1)
    return circuit

# Function to execute quantum circuit
def execute_circuit(circuit):
    simulator = Aer.get_backend('statevector_simulator')
    job = execute(circuit, simulator)
    result = job.result()
    statevector = result.get_statevector()
    return statevector

# Function to visualize quantum state
def visualize_quantum_state(statevector):
    return plot_bloch_multivector(statevector)

# Function to visualize quantum circuit
def visualize_quantum_circuit(circuit):
    circuit.draw('mpl')

# Function to create and execute quantum Fourier Transform
def quantum_fourier_transform(n_qubits):
    circuit = QuantumCircuit(n_qubits)
    for qubit in range(n_qubits):
        circuit.h(qubit)
        for next_qubit in range(qubit+1, n_qubits):
            circuit.cp(pi/2**(next_qubit-qubit), next_qubit, qubit)
    for qubit in range(n_qubits//2):
        circuit.swap(qubit, n_qubits-qubit-1)
    return circuit
