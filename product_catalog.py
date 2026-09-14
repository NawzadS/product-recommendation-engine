from product_data import products


# Print the first few products so I can see how the data is structured
print("First few products:")
for product in products[:5]:
    print(product)


# Store the customer's preferences in a list
customer_preferences = []

response = ""

while response != "N":
    print("Input a preference:")
    preference = input().lower()

    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# Convert the customer preferences to a set to remove duplicates
customer_preferences = set(customer_preferences)


# Convert each product's tags into a set
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# Count how many tags a product shares with the customer's preferences
def count_matches(product_tags, customer_tags):
    matches = product_tags.intersection(customer_tags)
    return len(matches)


# Recommend products that have at least one matching tag
def recommend_products(products, customer_tags):
    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(key=lambda product: product["matches"], reverse=True)

    return recommendations


# Get the recommendations
recommended_products = recommend_products(
    converted_products,
    customer_preferences
)


# Print the recommendations
print("\nRecommended Products:")

if len(recommended_products) == 0:
    print("No matching products found.")
else:
    for product in recommended_products:
        print(f'- {product["name"]} ({product["matches"]} match(es))')


# DESIGN MEMO
#
# For this program, I mainly used lists, sets, loops, functions, and set
# intersections. I started with a list because the customer can enter more
# than one preference and I needed somewhere to store each answer. After all
# of the preferences were entered, I converted the list into a set. I did
# this because a set removes duplicate values, so if someone enters the same
# preference more than once it will not affect the results. I also converted
# each product's tags into sets. This makes it easier to compare the product
# tags with the customer's preferences.
#
# The main operation I used to find matches was an intersection. The
# intersection gives me the values that are shared between the product tags
# and the customer preferences. I used len() on the intersection to count
# how many matches there were. I also used a loop to go through every
# product in the catalog. If a product had at least one match, I added its
# name and match count to the recommendations list. At the end, I sorted
# the recommendations so the products with the most matches appear first.
#
# If the catalog had over 1,000 products, looping through every single
# product would still work, but it could become slower as the catalog gets
# much larger. I could improve it by organizing products based on their
# tags ahead of time. For example, products with the "tech" tag could be
# stored together. Then the program could search only the groups that match
# the customer's preferences instead of checking every product. For a much
# larger store, the product information would probably also be stored in a
# database instead of directly inside a Python file.