# Step 1: Initial Feedback Data
1
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        'Very GOOD Service!!!',
        'poor support, not happy',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

n=int(input("Enter , how many feedback do you want to add"))
for i in range(n):
    print("Enter feedback",i+1)
    name=input("Enter Name :")
    feedback=input("Enter feedback :")
    rating=int(input("Enter rating (1-5):"))


    feedback_data['S_No'].append(len(feedback_data["S_No"])+1)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)

#print(feedback_data)
#print("Total",len(feedback_data["Feedback"]))

for j in range(len(feedback_data['Feedback'])):
    text=feedback_data['Feedback'][j]
    text=text.replace(","," ")
    text=text.replace("!"," ")
    text=text.replace("?"," ")
    text=text.replace("."," ")
    text=' '.join(text.split())
    text=text.lower()

    feedback_data["Feedback"][j]=text

   # print(text)

def word_count(word):
    count=0
    for feedback in feedback_data['Feedback']:
        words=feedback.split()

        if word.lower() in words:
            count+=1
    return count

print("Total",word_count("GOOD"))
print("Total",word_count("poor"))
print("Total",word_count("Excellent"))


print("Finale Cleaned Data",feedback_data)
print("Average Rating\n")
print(sum(feedback_data['Rating'])/len(feedback_data['Rating']))

new=set()
for feedback in feedback_data["Feedback"]:
   words=feedback.split()
   for word in words:
       new.add(word)
print("Unique Words:\n")
print(new)




longest=max(feedback_data["Feedback"],key=lambda x:len(x.split()))

print("longest Path\n",longest)

 
