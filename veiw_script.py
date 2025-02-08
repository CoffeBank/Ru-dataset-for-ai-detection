import json
import matplotlib.pyplot as plt
import numpy as np

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def summarize_by_source_and_dataset(data):
    summary = {}
    for record in data:
        source = record.get("source", "Unknown")
        dataset = record.get("dataset", "Unknown")
        
        if source not in summary:
            summary[source] = {}
        summary[source][dataset] = summary[source].get(dataset, 0) + 1
    return summary

def plot_grouped_bar_chart(summary): 
    sources = sorted(summary.keys())
    datasets = sorted({ds for source in summary for ds in summary[source].keys()})
    
    x = np.arange(len(sources))
    total_width = 0.8
    bar_width = total_width / len(datasets)
    
    cmap = plt.get_cmap("tab10")
    colors = {dataset: cmap(i) for i, dataset in enumerate(datasets)}
    
    plt.figure(figsize=(10, 6))
    
    for i, dataset in enumerate(datasets):
        counts = []
        for source in sources:
            count = summary[source].get(dataset, 0)
            counts.append(count)
        positions = x - total_width/2 + i*bar_width + bar_width/2
        plt.bar(positions, counts, width=bar_width, color=colors[dataset], label=dataset)
    
    plt.xlabel("Source")
    plt.ylabel("Number of records")
    plt.title("Comparison of 'source' by 'dataset'")
    plt.xticks(x, sources)
    plt.legend(title="Dataset")
    plt.tight_layout()
    plt.show()

def main():
    filename = 'ru_detection_dataset.json'
    data = load_json(filename)
    summary = summarize_by_source_and_dataset(data)
    plot_grouped_bar_chart(summary)

if __name__ == '__main__':
    main()
