import time
import random
import json
from pathlib import Path
from tqdm import tqdm
from hallucinator.core import HallucinationDetector

def generate_test_text(num_samples=100):
    """Generate benchmark samples with different risk levels"""
    samples = []
    for _ in range(num_samples):
        if random.random() < 0.3:
            # High-risk sample
            text = f"Reported {random.randint(1,100)} cases in {random.randint(2020,2030)}. " \
                   f"Some sources claim {random.randint(1,100)} cases."
        else:
            # Low-risk sample
            text = "Standard factual statement without controversial claims."
        samples.append(text)
    return samples

def run_benchmark():
    detector = HallucinationDetector()
    samples = generate_test_text()
    
    print(f"Benchmarking with {len(samples)} samples...")
    
    results = {
        'total_time': 0,
        'avg_latency': 0,
        'memory_usage': [],
        'risk_distribution': []
    }
    
    start_time = time.time()
    
    for text in tqdm(samples):
        t0 = time.perf_counter()
        result = detector.analyze(text)
        t1 = time.perf_counter()
        
        results['total_time'] += t1 - t0
        results['risk_distribution'].append(result['risk_score'])
    
    results['avg_latency'] = results['total_time'] / len(samples)
    
    # Save results
    output_path = Path("benchmark_results.json")
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {output_path}")
    print(f"Average latency: {results['avg_latency']:.4f}s per analysis")

if __name__ == "__main__":
    run_benchmark()