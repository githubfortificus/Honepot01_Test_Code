def main():
    # Please remember to change your database username and password as this is now Internet facing

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
        ICMPTYPE = 0
        ICMPCODE = 0
        FROM_DOMAIN = ""
        TO_DOMAIN = ""
        GeoIP = ""
        Priority = "0"
        Notes = ""

        print SOURCEIP, SOURCEPORT


        mysqldb_cursor.execute('insert into test3 (Date, Time, Action, Protocol, SRCIP, SRCP, DSTIP, DSTP, Flags, ICMPTYPE, ICMPCODE, Full_message) \
                                values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%d", "%d", "%s")' % \
                                (DATE, HOUR, ACTION, PROTOCOL, SOURCEIP, SOURCEPORT, DESTINATIONIP, DESTINATIONPORT, FLAGS_INS, ICMPTYPE, ICMPCODE, line))
        mysqldb.commit()

    file.close()
    mysqldb_cursor.close()

main()