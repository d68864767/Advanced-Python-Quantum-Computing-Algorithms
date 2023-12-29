# main.py

# Importing required libraries
import config
import quantum_algorithms as qa
from qiskit.visualization import plot_bloch_multivector

def main():
    # Load OpenAI API key
    openai_api_key = config.OPENAI_API_KEY
    if openai_api_key is None:
        print("Failed to load OpenAI API key. Exiting...")
        return

    # Create Bell State
    bell_state_circuit = qa.create_bell_state()

    # Execute the circuit
    statevector = qa.execute_circuit(bell_state_circuit)

    # Visualize the quantum state
    plot_bloch_multivector(statevector)

    # Create and execute Quantum Fourier Transform
    qft_circuit = qa.quantum_fourier_transform(3)
    qft_statevector = qa.execute_circuit(qft_circuit)

    # Visualize the quantum state
    plot_bloch_multivector(qft_statevector)

if __name__ == "__main__":
    main()
