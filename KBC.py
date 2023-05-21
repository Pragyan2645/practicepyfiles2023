# KBC Console

#Registration Details


print("KBC Registration")
name = input("Enter your good name:")
age = int(input("Enter your age:"))
email = input("Enter your Email-ID:")
regdate = input("Enter date of registeration:(yyyy-mm-dd)")
print("Hii!", name, "Your registration succeeded! \n BEST OF LUCK!", name)

# Instructions
print(  "INSTRUCTIONS\n1.Total 10 questions\n2.Questions are MCQ Based\n3.All Questions are compulsory\n4.Every correct question will reward you 10,000 Rupees\nHere are your questions")

# Question and reward apparatus
prize=0
count=0
q1 = input("1.‘Mahila Nidhi’ is the first ever women’s cooperative fund launched by which state/UT?\n[A] Kerala\n[B] Rajasthan\n[C] Karnataka\n[D] Andhra Pradesh")

if q1.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B [Rajasthan]\n Notes:Mahila Nidhi is the first-ever women’s cooperative fund launched by Rajasthan. Rajasthan Chief Minister Ashok Gehlot approved a proposal for giving 8% interest subsidy on loans obtained by the members of women’s self-help groups (SHGs) from Mahila Nidhi.Mahila Nidhi is operated entirely by women and acts as a complementary body with the formal banking system.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")


q2 = input("2. Which country is the host of the Bilateral Maritime exercise ‘SLINEX-2023’?\n[A] India\n[B] Sri Lanka\n[C] France\n[D] Singapore")

if q2.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B[Sri Lanka]\n Notes:In a non-binding referendum held in France, 89.03% of the votes cast were opposed to the freestanding scooters, which are booked on a short-term basis through apps.The rental e-scooters, which were introduced in 2018 to promote green alternative for cars. The city will completely ban these devices by September 1 this year.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)


print("Next Question")

q3 = input("3. ‘Proba-3 Mission’, which will be launched aboard ISRO’s PSLV, is associated with which space agency?\n[A] NASA\n[B] ESA\n[C] JAXA\n[D] CNSA ")

if q3.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B [ESA] \nNotes:The European Space Agency’s Proba-3 Mission will be launched aboard the ISRO’s PSLV in 2024. Its two satellites will study the Sun’s faint corona and surrounding atmosphere.The 340-kilogram spacecraft will be deployed by PSLV in a high Earth orbit with an orbital period of 19.7 hours.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")

q4 = input("4.When is the ‘International Day of Zero Wastes’ observed?\n[A] March 25\n[B] March 30\n[C] April 5\n[D] April 10")

if q4.upper() != 'B':
  print("Wrong Answer!\nCorrect answer B [March 30]\nNotes:International Day of Zero Wastes is observed on March 30 every year. The theme for this year is ‘Achieving sustainable and environmentally sound practices of minimizing and managing waste’.The International Day of Zero Waste aims to promote sustainable consumption and production patterns, support the societal shift towards circularity and raise awareness about how zero-waste initiatives contribute to the advancement of the 2030 Agenda for Sustainable Development.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")

q5 = input("5.Captive Employment Initiative was launched under which scheme?\n[A] Deen Dayal Upadhyaya Kaushalya Yojana\n[B] MGNREGA\n[C] Mission Antyodaya\n[D] Pradhan Mantri Gram Sadak Yojana")

if q5.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B [Deen Dayal Upadhyaya Kaushalya Yojana]\nNotes:Captive Employment Initiative was launched by the Central Government under the Deen Dayal Upadhyaya Kaushalya Yojana.Under this initiative, captive employers will train rural poor youth and provide them with jobs in their company or subsidiary.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")

q6 = input("6.Which state/UT hosted the ‘First International Quantum Communication Conclave’?\n[A] Maharashtra\n[B] New Delhi\n[C] Gujarat\n[D] Karnataka")

if q6.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B [New Delhi]\nNotes:The first International Quantum Communication Conclave was held on March 28 and 29 this year in Delhi.It was organized by the Department of Telecommunications in collaboration with the CDOT, Telecommunications Standards Development Society India (TSDSI) and IEEE Communications Society.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")

q7 = input("7.Nationwide Artificial Insemination Programme is being implemented under which scheme?\n[A] Rashtriya Gokul Mission\n[B] National Livestock Mission\n[C] Livestock Health and Disease Control\n[D] National Programme for Dairy Development")

if q7.upper() != 'A':
  print("Wrong Answer!\nCorrect Answer: A [Rashtriya Gokul Mission]\nNotes:Nationwide Artificial Insemination Programme (NAIP) is being implemented under the Rashtriya Gokul Mission scheme to promote livestock industry in India.\nThe implementation of the Artificial Insemination method and other initiatives resulted in milk production in India increasing from 146.31 Million Tonnes in 2014-15 to 220.78 Million in 2021-22. ")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Question")

q8 = input("8.Which Union Ministry implements the ‘Saansad Adarsh Gram Yojana’?\n[A] Ministry of Rural Development\n[B] Ministry of Housing and Urban Affairs\n[C] Ministry of Agriculture and Farmers Welfare\n[D] Ministry of MSME")

if q8.upper() != 'A':
  print("Wrong Answer!\nCorrect Answer: A [Ministry of Rural Development]\nNotes:Saansad Adarsh Gram Yojana was launched by the Central Government to promote the development of rural India. Operational guidelines to implement this scheme was unveiled recently.The scheme aims to develop Gram Panchayats is envisaged through implementation of existing Government Schemes and Programmes in convergence mode and mobilization of community and private resources.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)

print("Next Questions")

q9 = input("9.CBIC has notified exemption from Customs duty and Agriculture Infrastructure development Cess on which product?\n[A] Jute\n[B] Raw Cotton\n[C] Silk yarn\n[D] Palm Oil")

if q9.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: B [Raw Cotton]\nNotes:The Central Board of Indirect Taxes and Customs (CBIC) notified the exemption from Customs duty and Agriculture Infrastructure development Cess for import of cotton.\nThis exemption would benefit the textile chain- yarn, fabric, garments and made ups and provide relief to textile industry and consumers. Industry has been demanding for removal of 5% Basic Customs Duty (BCD) and 5% Agriculture Infrastructure and Development Cess (AIDC) on raw cotton.")
  count+=1
  print("Current Status of PrizeMoney:",prize)
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)


print("Next Question")

q10 = input("10.Which multi-national company has announced to provide grant to protect the mangrove ecosystem in Maharashtra’s Raigad?\n[A] Microsoft\n[B] Google\n[C] Apple\n[D] SpaceX")
if q10.upper() != 'B':
  print("Wrong Answer!\nCorrect Answer: C [Apple]\nNotes:Apple Inc has announced to protect the 2,400-hectare mangrove ecosystem in Maharashtra’s Raigad district.\nWith a grant from the tech giant, Applied Environmental Research Foundation (AERF) will work with the local community to protect the mangrove forest. Apple’s grant will support the restoration of mangroves across a 50-hectare area where they have degraded. It will also distribute portable bio-stoves that allow people to cook without cutting down mangroves for firewood.")
  count+=1
else:
  print("Correct answer\n Rewarded by 10,000 Rupees")
  prize+=10000
  print("Current Status of PrizeMoney:",prize)


# Afterward competition formalties

print("YOUR PRIZEMONEY:",prize)

if prize != 100000:
  print("Total wrong questions:",count)

else: 
  print("ALL ANSWERS ARE CORRECT!!!")

print("THANKS FOR GIVING YOUR PRECIOUS TIME",name)