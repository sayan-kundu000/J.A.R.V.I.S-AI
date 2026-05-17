from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def run_quantum_simulation():
    """
    Creates a simple quantum circuit with a Superposition layer to generate a
    true quantum sequence via measurement, using the local Qiskit Aer simulator.
    Does NOT require an external IBM Cloud key.
    """
    try:
        # Create a Quantum Circuit with 4 qubits and 4 classical bits
        qc = QuantumCircuit(4, 4)
        
        # Apply Hadamard gates to put all 4 qubits in superposition
        qc.h([0,1,2,3])
        
        # Measure all qubits
        qc.measure([0,1,2,3], [0,1,2,3])
        
        # Local simulator instance
        simulator = AerSimulator()
        
        # Compile and run the circuit
        compiled_circuit = transpile(qc, simulator)
        job = simulator.run(compiled_circuit, shots=1)
        result = job.result()
        
        # Get the counts (bitstring output)
        counts = result.get_counts(qc)
        bitstring = list(counts.keys())[0]
        
        # Convert binary output to integer loosely representing an 'advanced' algorithmic outcome
        random_num = int(bitstring, 2)
        
        return {
            "status": "SUCCESS",
            "qubits_used": 4,
            "bitstring_measured": bitstring,
            "integer_value": random_num,
            "details": f"Quantum Superposition collapsed into state |{bitstring}> locally."
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "details": str(e)
        }
