inputData = """Aaron Abigail Adam Adrian Aisha Alan Albert Alexa Alice Amanda Amir Amy Andrew Angela Anita Anna Anthony Antonio April Arjun Ashley Audrey Austin Barbara Benjamin Beth Betty Brandon Brenda Brian Brittany Bruce Caleb Cameron Carla Carlos Carmen Carol Catherine Charles Charlotte Chloe Chris Christian Christina Christopher Claire Clara Claudia Cody Colin Connor Courtney Craig Cynthia Daniel Danielle David Deborah Dennis Diana Diego Dominic Donna Doris Dorothy Dylan Edward Elaine Elizabeth Ella Emily Emma Eric Ethan Eva Evelyn Faith Felicia Fiona Frances Frank Gabriel Gail Gary George Gerald Gina Gloria Grace Gregory Hannah Harold Heather Henry Holly Ian Irene Isaac Isabella Jack Jacob James Jamie Janet Jared Jason Jasmine Jean Jeffrey Jennifer Jeremy Jerry Jessica Jill Joan Joe John Johnny Jordan Jose Joseph Joshua Julia Julian Justin Karen Katherine Kathleen Kathryn Kayla Keith Kelly Kenneth Kevin Kimberly Kyle Laura Lauren Leah Leonard Liam Linda Lisa Logan Lori Louis Lucas Lucy Luke Madison Maggie Manuel Maria Marie Marilyn Mark Martha Martin Mary Mason Matthew Megan Melissa Michael Michelle Miguel Molly Monica Morgan Nancy Natalie Nathan Neil Nicholas Nicole Noah Nora Olivia Oscar Pamela Patricia Patrick Paul Paula Peter Philip Rachel Ralph Randy Raymond Rebecca Richard Robert Roger Ronald Rose Roy Russell Ryan Samantha Samuel Sandra Sara Sarah Scott Sean Sebastian Sharon Sheila Sophia Stephanie Stephen Steven Susan Sylvia Taylor Teresa Thomas Tiffany Timothy Tina Todd Trevor Tyler Valerie Vanessa Victor Victoria Vincent Violet Virginia"""
codes = inputData.split()

#codes = inputData.split(',')
#codes = inputData.split(",")

template = {
    "id" :"1",
    "Enrolled":"yes",
    "isActive":True
}

result= []
for code in codes:
    value = {"name": code}
    value.update(template)
    result.append(value)

    #print(result)

    #Split operation

words="Hii","Welcome"
joined = " ".join(words)
print(joined)

  # to replace a word

content = "I Know Java"
Newcontent = content.replace("Java","Python")
print(Newcontent)
    
   #Change to Upper and Lower case
name = "vetha"
name = name.upper()
print(name)

name = "VETHA"
name = name.lower()
print(name)