$year = $args[0]
$day = $args[1].ToString().PadLeft(2, '0')

Function createEntry() {
    $day_path = ".\$year\$day"
    if (Test-Path -Path $day_path) {
        "Entry already exists"
    }
    else {
        New-Item -ItemType Directory -Path $day_path
        New-Item -ItemType File -Path "$day_path\part1.py"
        New-Item -ItemType File -Path "$day_path\part2.py"
        New-Item -ItemType File -Path "$day_path\sample.txt"
        New-Item -ItemType File -Path "$day_path\input.txt"
    }
}

if (Test-Path -Path $year) {
    createEntry
}
else {
    New-Item -ItemType Directory -Path $year
    createEntry
}