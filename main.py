import os
import matplotlib.pyplot as plt


def read_abstracts(folder):
    abstracts = {}

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)

            with open(path, "r") as file:
                abstracts[filename] = file.read()

    return abstracts


def count_entities(text):
    entity_categories = {
        "genes_proteins": ["pcsk9", "ldlr", "ldl"],
        "drugs": [
            "statins",
            "inhibitors",
            "antibodies",
            "evolocumab",
            "alirocumab",
            "inclisiran"
        ],
        "diseases": [
            "hypercholesterolemia",
            "cardiovascular disease",
            "atherosclerosis"
        ]
    }

    text = text.lower()
    results = {}

    for category, entities in entity_categories.items():
        category_counts = {}

        for entity in entities:
            count = text.count(entity)

            if count > 0:
                category_counts[entity] = count

        results[category] = category_counts

    return results


def combine_results(all_results):
    combined = {}

    for results in all_results.values():
        for category, entities in results.items():
            if category not in combined:
                combined[category] = {}

            for entity, count in entities.items():
                combined[category][entity] = combined[category].get(entity, 0) + count

    return combined


def save_report(combined_results):
    with open("pcsk9_report.txt", "w") as file:
        file.write("PCSK9 MULTI-ABSTRACT ANALYSIS REPORT\n")
        file.write("-------------------------------------\n\n")

        for category, entities in combined_results.items():
            file.write(category.replace("_", " ").title() + ":\n")

            for entity, count in entities.items():
                file.write(f"- {entity} ({count} mentions)\n")

            file.write("\n")


def save_csv(combined_results):
    with open("entity_counts.csv", "w") as file:
        file.write("category,entity,count\n")

        for category, entities in combined_results.items():
            for entity, count in entities.items():
                file.write(f"{category},{entity},{count}\n")


def save_entity_plot(combined_results):
    entities = []
    counts = []

    for category_entities in combined_results.values():
        for entity, count in category_entities.items():
            entities.append(entity)
            counts.append(count)

    plt.figure(figsize=(9, 5))
    plt.bar(entities, counts)
    plt.title("PCSK9 Multi-Abstract Entity Frequencies")
    plt.xlabel("Entity")
    plt.ylabel("Mentions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("entity_plot.png")


abstracts = read_abstracts("abstracts")

all_results = {}

for filename, abstract_text in abstracts.items():
    all_results[filename] = count_entities(abstract_text)

combined_results = combine_results(all_results)

print("PCSK9 MULTI-ABSTRACT RESEARCH ASSISTANT")
print("---------------------------------------")

for category, entities in combined_results.items():
    print("\n" + category.replace("_", " ").title() + ":")

    for entity, count in entities.items():
        print(f"- {entity} ({count} mentions)")

save_report(combined_results)
save_csv(combined_results)
save_entity_plot(combined_results)

print("\nReport saved to pcsk9_report.txt")
print("CSV saved to entity_counts.csv")
print("Plot saved to entity_plot.png")