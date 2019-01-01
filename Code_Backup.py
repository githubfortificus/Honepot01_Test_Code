            print "TCP Protocol Detected..."
            text = line.split()
            if line.find("DF") == 1:
                print "DF not here"
                PROTO = text[18]
                print PROTO
            else:
                print "DF here..."
                PROTO = text [19]
                print PROTO
        elif line.find("PROTO=UDP") == 1:
            print "UDP Protocol Detected..."
            text = line.split()
            PROTO = text[18]
            print PROTO
        else:
            print "Strange Protocol detected..."






            def main():

    import MySQLdb
    import datetime

    mysqldb = MySQLdb.connect (host="172.16.100.129", port=3306, user="syslog", passwd="sys10g01!", db="Syslog")

    mysqldb_cursor = mysqldb.cursor()

    file = open("../RAW/test.log", "r")

    for line in file:
        text = line.split()
        DATE = datetime.date(2018, 12, int(text[1]))
        TIMESTR = text[2].replace(':',' ').split()
        HOUR = datetime.time(int(TIMESTR[0]), int(TIMESTR[1]), int(TIMESTR[2]))
        ACTION = text[7].replace(':','')
        PROTOCOL = text[18].replace('PROTO=','')
        SOURCEIP = text[11].replace('SRC=','')
        SOURCEPORT = text[19].replace('SPT=','')
        DESTINATIONIP = text[12].replace('DST=','')
        DESTINATIONPORT = text[20].replace('DPT=','')
        FLAGS = text[23:]
        FLAGS_INS = " ".join(FLAGS)
        ICMPTYPE = ""
        ICMPCODE = ""
        FROM_DOMAIN = ""
        TO_DOMAIN = ""
        GeoIP = ""
        Priority = "0"
        Notes = ""

        mysqldb_cursor.execute('insert into test2 (Date, Time) values ("%s", "%s")' % (DATE, HOUR))
        mysqldb.commit()

    file.close()
    mysqldb_cursor.close()

main()