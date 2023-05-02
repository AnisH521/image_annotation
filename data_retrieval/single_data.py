import psycopg2
from PIL import Image
import io

conn = psycopg2.connect(host = "dpg-ch7rfo82qv2864obrud0-a.oregon-postgres.render.com",
                        port = 5432, 
                        database = "image_database", 
                        user = "image_database_user", 
                        password = "2ygmOfAGddzefeniRaRWRtR77mQwyvUu")

query = "SELECT img FROM image_database WHERE id = 3"

cur = conn.cursor()
cur.execute(query, (1,))
image_data = cur.fetchone()[0]

image = Image.open(io.BytesIO(image_data))
image.save("image.png")

cur.close()
conn.close()