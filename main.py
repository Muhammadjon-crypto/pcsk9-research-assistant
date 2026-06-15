def read_abstract(filename):
    with open(filename, "r") as file:
        return file.read()


def find_entities(text):
    genes_proteins = ["pcsk9", "ldlr", "ldl"]
    drugs = ["statins", "inhibitors", "antibodies"]
    diseases = ["hypercholesterolemia", "cardiovascular disease"]

    text = text.lower()

    found_genes = [item for item in genes_proteins if item in text]
    found_drugs = [item for item in drugs if item in text]
    found_diseases = [item for item in diseases if item in text]

    return found_genes, found_drugs, found_diseases


def save_report(genes, drugs, diseases):
    with open("pcsk9_report.txt", "w") as file:
        file.write("PCSK9 RESEARCH ASSISTANT REPORT\n")
        file.write("--------------------------------\n\n")

        file.write("Genes / Proteins:\n")
        for item in genes:
            file.write(f"- {item}\n")

        file.write("\nDrugs:\n")
        for item in drugs:
            file.write(f"- {item}\n")

        file.write("\nDiseases:\n")
        for item in diseases:
            file.write(f"- {item}\n")


abstract = read_abstract("abstract.txt")

genes, drugs, diseases = find_entities(abstract)

print("PCSK9 RESEARCH ASSISTANT")
print("------------------------")

print("\nGenes / Proteins:")
for item in genes:
    print("-", item)

print("\nDrugs:")
for item in drugs:
    print("-", item)

print("\nDiseases:")
for item in diseases:
    print("-", item)

save_report(genes, drugs, diseases)

print("\nReport saved to pcsk9_report.txt")