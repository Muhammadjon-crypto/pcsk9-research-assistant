def read_abstract(filename):
    with open(filename, "r") as file:
        return file.read()


def find_entities(text):
    entity_categories = {
        "genes_proteins": ["pcsk9", "ldlr", "ldl"],
        "drugs": ["statins", "inhibitors", "antibodies", "evolocumab", "alirocumab", "inclisiran"],
        "diseases": ["hypercholesterolemia", "cardiovascular disease", "atherosclerosis"]
    }

    text = text.lower()
    results = {}

    for category, entities in entity_categories.items():
        found = []

        for entity in entities:
            if entity in text:
                found.append(entity)

        results[category] = found

    return results


def save_report(results):
    with open("pcsk9_report.txt", "w") as file:
        file.write("PCSK9 RESEARCH ASSISTANT REPORT\n")
        file.write("--------------------------------\n\n")

        for category, entities in results.items():
            file.write(category.replace("_", " ").title() + ":\n")

            for entity in entities:
                file.write(f"- {entity}\n")

            file.write("\n")


def save_csv(results):
    with open("entity_counts.csv", "w") as file:
        file.write("category,entity,count\n")

        for category, entities in results.items():
            for entity in entities:
                file.write(f"{category},{entity},1\n")


abstract = read_abstract("abstract.txt")

results = find_entities(abstract)

print("PCSK9 RESEARCH ASSISTANT")
print("------------------------")

for category, entities in results.items():
    print("\n" + category.replace("_", " ").title() + ":")

    for entity in entities:
        print("-", entity)

save_report(results)
save_csv(results)

print("\nReport saved to pcsk9_report.txt")
print("CSV saved to entity_counts.csv")