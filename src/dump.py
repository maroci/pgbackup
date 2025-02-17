from pgbackup import pgdump

dump = pgdump.dump('postgres://demo:secure-password@34.244.44.109:5432/sample')
file = open('dump.sql','w+b')
file.write(dump.stdout.read())
file.close()

