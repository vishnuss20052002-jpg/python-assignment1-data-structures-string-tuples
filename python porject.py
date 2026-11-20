# Project: Survey Feedback Analyzer


# STEP 1: Preloaded Feedbacks (Given Data)

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj',
             'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],

    'Feedback': [
        '    Very GOOD Service!!!',
        'poor support,   not happy   ',
        'GREAT experience! will come again.',
        'okay   okay...',
        '   not   BAD',
        'Excellent care, excellent staff!!',
        'good food and good ambience!!',
        'Poor response and poor handling of issue',
        'Satisfied, But could be better.',
        'Good support... quick service.'
    ],

    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}


# STEP 2: Add More Feedbacks

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):

    print("\nEnter Feedback Details")

    name = input("Enter Name: ")

    feedback = input("Enter Feedback: ")

    rating = int(input("Enter Rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Invalid Rating! Please enter between 1 and 5.")
        rating = int(input("Enter Rating (1-5): "))

    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)

    feedback_data['Name'].append(name)

    feedback_data['Feedback'].append(feedback)

    feedback_data['Rating'].append(rating)


# STEP 3: Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')

    text = ' '.join(text.split())

    text = text.lower()

    feedback_data['Feedback'][i] = text


print("\n========== CLEANED FEEDBACK DATA ==========")

print(feedback_data)


# STEP 4: Word Count Insights

def count_word_in_feedbacks(word):

    count = 0

    for feedback in feedback_data['Feedback']:

        if word.lower() in feedback.split():

            count += 1

    return count


print("\n========== WORD COUNT INSIGHTS ==========")

print("Feedbacks containing 'good':",
      count_word_in_feedbacks('good'))

print("Feedbacks containing 'poor':",
      count_word_in_feedbacks('poor'))

print("Feedbacks containing 'excellent':",
      count_word_in_feedbacks('excellent'))


# STEP 5: Final Summary & Insights

print("\n========== FINAL SUMMARY ==========")

print("\nFinal Cleaned Feedback Data:")

print(feedback_data)


# Average Rating

total_rating = sum(feedback_data['Rating'])

total_feedbacks = len(feedback_data['Rating'])

average_rating = total_rating / total_feedbacks

print("\nAverage Rating:", round(average_rating, 2))


# Longest Feedback

longest_feedback = max(
    feedback_data['Feedback'],
    key=lambda x: len(x.split())
)

print("\nLongest Feedback:")

print(longest_feedback)

print("Word Count:", len(longest_feedback.split()))


# Unique Words

unique_words = set()

for feedback in feedback_data['Feedback']:

    words = feedback.split()

    for word in words:

        unique_words.add(word)


print("\nUnique Words Used Across All Feedbacks:")

print(sorted(unique_words))


# Optional: Sort Feedbacks by Rating (Highest to Lowest)

print("\n========== SORTED FEEDBACKS ==========")

sorted_feedbacks = sorted(
    zip(feedback_data['Name'],
        feedback_data['Feedback'],
        feedback_data['Rating']),
    key=lambda x: x[2],
    reverse=True
)

for name, feedback, rating in sorted_feedbacks:

    print(name, "|", feedback, "| Rating:", rating)


print("\n========== PROJECT COMPLETED ==========")
