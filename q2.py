borrowed_books = input("Enter books as 'Title - Days, Title - Days': ").split(", ")
books = {}
for record in borrowed_books:
    title, days = record.split(" - ")
    books[title] = books.get(title, 0) + int(days)

most_borrowed = max(books, key=books.get)
least_borrowed = min(books, key=books.get)

average_days = sum(books.values()) / len(books)

sorted_books = sorted(books.items(), key=lambda x: x[1], reverse=True)

# Print results
print(f"Most borrowed: {most_borrowed} ({books[most_borrowed]} days)")
print(f"Least borrowed: {least_borrowed} ({books[least_borrowed]} days)")
print(f"Average borrowing time: {average_days:.2f} days")
print("Books sorted by borrowing duration (descending):")
for title, days in sorted_books:
    print(f"{title}: {days} days")