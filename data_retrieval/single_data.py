import psycopg2
from PIL import Image
import io

conn = psycopg2.connect(host = "hostname",
                        port = 5432, 
                        database = "image_database", 
                        user = "image_database_user", 
                        password = "***************")

query = "SELECT img FROM image_database WHERE id = 3"

cur = conn.cursor()
cur.execute(query, (1,))
image_data = cur.fetchone()[0]

image = Image.open(io.BytesIO(image_data))
image.save("image.png")

cur.close()
conn.close()
