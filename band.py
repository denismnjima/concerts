from db_connection import database_connect

class Band:
    def __init__(self,id):
        self.id = id
    def concerts(self):
        conn = database_connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT concert.concert_name, 
                         concert.date,
                         venue.title 
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                         INNER JOIN venue ON venue.venue_id = concert.venue_id
                WHERE band.band_id= %s
            '''), (self.id,))
            concerts = cur.fetchall()
            cur.close()
            conn.close()
            return concerts
        else:
            return []
    def venues(self):
        conn = database_connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT venue.city, 
                         venue.title 
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                         INNER JOIN venue ON venue.venue_id = concert.venue_id
                WHERE band.band_id= %s
            '''), (self.id,))
            venues = cur.fetchall()
            cur.close()
            conn.close()
            return venues
        else:
            return []
        
    def play_in_venue(self, venue, date, concert_name):
        conn = database_connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                INSERT INTO concert (band_id, venue_id, date, concert_name)
                VALUES (%s, %s, %s, %s)
            '''), (self.id, venue, date, concert_name))
            conn.commit()
            cur.close()
            conn.close()
            return True
        else:
            return False
    def all_introductions(self):
        conn = database_connect()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT band.hometown,
                         venue.city,
                         band.name            
                FROM concert
                INNER JOIN band ON concert.band_id = band.band_id
                INNER JOIN venue ON venue.venue_id = concert.venue_id
                WHERE band.band_id= %s
                
            '''), (self.id,))
            hometown = cur.fetchone()
            cur.close()
            conn.close()
            return f"Hello {hometown[1]}!!!!! We are {hometown[2]} and we're from {hometown[0]}"


