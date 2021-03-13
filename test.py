import pymysql

conn = pymysql.connect(
    host="localhost", port=3306, user="oscar",
    password="oscar", db="sakila"
)

cursor = conn.cursor()

query1 = """
SELECT * FROM film_actor
INNER JOIN film
ON film_actor.film_id = film.film_id
WHERE actor_id < 10
"""


# cursor.execute(query1)
# result = cursor.fetchall()
# print(len(result))

# # cursor.execute(query2)

# # result = cursor.fetchall()
# # print(len(result))
# # for row in result:
# #     print(row)


# conn.commit()
