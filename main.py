import os

# Llegim tots els

all_files = os.listdir("countries/")
print(all_files.__sizeof__())
countries_with_religious = []
countries_with_humanist = []
countries_with_admin = []
countries_with_setup = []


reli_count = 0
humanist_count = 0
admin_count = 0
ARwithoutEc_count = 0
total = 0

print (True and True and not False)

for file in all_files :
    total += 1
    with open("countries/{}".format(file), 'r') as fd:
        Lines = fd.readlines();
        has_reli = False
        has_admin = False
        has_inno = False
        has_eco = False
        has_human = False
        has_expan = False
        found_desired = False
        for line in Lines:
            if line.strip() == "religious_ideas":
                reli_count += 1
                countries_with_religious.append(file)
                has_reli = True
            if line.strip() == "humanist_ideas":
                humanist_count += 1
                countries_with_humanist.append(file)
                has_human = True
            if line.strip() == "administrative_ideas":
                admin_count +=1
                countries_with_admin.append(file)
                has_admin = True
            if line.strip() == "innovativeness_ideas":
                has_inno = True
            if line.strip() == "economic_ideas":
                has_eco = True
            if line.strip() == "expansion_ideas":
                has_expan = True

        if (has_reli and has_admin and not has_eco and not found_desired):
            countries_with_setup.append(file)
            found_desired = True


print("Found {} countries with religious ideas, that is {}%".format(reli_count, (reli_count / total) * 100))
print(countries_with_religious)
print("\nFound {} countries with humanist ideas, that is {}% ".format(humanist_count, (humanist_count / total) * 100))
print(countries_with_humanist)
print("\nFound {} countries with administrative, that is {}% ".format(admin_count, (admin_count / total) * 100))
print(countries_with_admin)
xd_count = len(countries_with_setup)
print("\nFound {} countries with the desired setup, that is {}% ".format(xd_count, (xd_count / total) * 100))
print(countries_with_setup)