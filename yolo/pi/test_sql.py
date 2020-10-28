#import sqlite3


#conn = sqlite3.connect('data/result/test.sqlite')

#cur = conn.cursor()

#cur.execute('CREATE TABLE test (time VARCHAR, object VARCHAR)')
#cur.execute('INSERT INTO test (time, description) values ("Aquiles", "My test description")')

#conn.commit()

#conn.close
from datetime import datetime, timezone

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.now(timezone.utc).astimezone().isoformat("T", "seconds"))