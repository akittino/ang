import pymysql
import random

config = {
  'user': 'root',
  'passwd': 'mlekomleko15',
  'host': '127.0.0.1',
  'db': 'kanty',
  'unix_socket': '/tmp/mysql.sock',
  'charset': 'utf8'
}


def get_question(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM question WHERE type = "%s" ORDER BY RAND() LIMIT 4' % "rzeczownik")
    data = cur.fetchall()
    cur.close()
    return data


def play_game(conn):
    data = get_question(conn)
    selected = random.randint(0, 3)
    print("which answer for %s:" % data[selected][1])

    for q in data:
        print("\t %s" % q[2])
    if int(input()) - 1 == selected:
        print("Good.", end='')
    else:
        print("Nope.", end='')
    print(" it was %s -> %s\n" % (data[selected][1], data[selected][2]))


def main():
    conn = pymysql.connect(**config)
    for _ in range(2):
        play_game(conn)
    conn.close()


if __name__ == "__main__":
    main()