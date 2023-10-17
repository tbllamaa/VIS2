# List of volcano types
volcano_types = [
    "Stratovolcano",
    "Stratovolcano",
    "Complex volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Shield volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Subglacial volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Shield volcano",
    "Shield volcano",
    "Shield volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Lava dome",
    "Stratovolcano",
    "Stratovolcano",
    "Complex volcano",
    "Shield volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Lava dome",
    "Stratovolcano",
    "Stratovolcano",
    "Caldera",
    "Stratovolcano",
    "Caldera",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Complex volcano",
    "Caldera",
    "Shield volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Stratovolcano",
    "Shield volcano",
    "Stratovolcano",
    "Stratovolcano",
    "Shield volcano",
    "Shield volcano",
]

# Count the occurrences of each volcano type
volcano_type_counts = {}
for volcano_type in volcano_types:
    if volcano_type in volcano_type_counts:
        volcano_type_counts[volcano_type] += 1
    else:
        volcano_type_counts[volcano_type] = 1

# Print the counts of each volcano type
for volcano_type, count in volcano_type_counts.items():
    print(f"{volcano_type}: {count} times")
