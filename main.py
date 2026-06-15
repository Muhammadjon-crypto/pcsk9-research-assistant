import matplotlib.pyplot as plt


def read_abstract(filename):
    with open(filename, "r") as file:
        return file.read()


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


def save_report(results):
    with open("pcsk9_report.txt", "w") as file:
        file.write("PCSK9 RESEARCH ASSISTANT REPORT\n")
        file.write("--------------------------------\n\n")

        for category, entities in results.items():
            file.write(category.replace("_", " ").title() + ":\n")

            for entity, count in entities.items():
                file.write(f"- {entity} ({count} mentions)\n")

            file.write("\n")


def save_csv(results):
    with open("entity_counts.csv", "w") as file:
        file.write("category,entity,count\n")

        for category, entities in results.items():
            for entity, count in entities.items():
                file.write(f"{category},{entity},{count}\n")


def save_entity_plot(results):
    entities = []
    counts = []

    for category_entities in results.values():
        for entity, count in category_entities.items():
            entities.append(entity)
            counts.append(count)

    plt.figure(figsize=(9, 5))
    plt.bar(entities, counts)
    plt.title("PCSK9 Research Entity Frequencies")
    plt.xlabel("Entity")
    plt.ylabel("Mentions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("entity_plot.png")


abstract = read_abstract("abstract.txt")
results = count_entities(abstract)

print("PCSK9 RESEARCH ASSISTANT")
print("------------------------")

for category, entities in results.items():
    print("\n" + category.replace("_", " ").title() + ":")

    for entity, count in entities.items():
        print(f"- {entity} ({count} mentions)")

save_report(results)
save_csv(results)
save_entity_plot(results)

print("\nReport saved to pcsk9_report.txt")
print("CSV saved to entity_counts.csv")
print("Plot saved to entity_plot.png")