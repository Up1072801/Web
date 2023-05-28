import sqlite3,datetime,time,os

def load_data():
    global conn
    loanedto = [
(1,"Museo del Prado",datetime.date(2022,1,1),datetime.date(2022,12,31)),
(2,"Museo del Prado",datetime.date(2022,1,1),datetime.date(2022,12,31)),
(3,"Louvre",datetime.date(2022,1,1),datetime.date(2022,12,31)),
(4,"British Museum",datetime.date(2023,1,1),datetime.date(2023,12,31)),
(5,"British Museum",datetime.date(2023,1,1),datetime.date(2023,12,31))
]
    Idioktitos = [(1,),(2,),(3,),(4,),(5,),(6,),(7,),(8,),(9,),(10,),(11,),(12,),(13,),(14,),(15,),(16,),(17,)]
    loanedpaintings=[
                 (17,datetime.date(2022,1,1),datetime.date(2023,1,1),"National Gallery (London)"),
                 (18,datetime.date(2022,1,1),datetime.date(2023,1,1),"National Gallery (London)"),
                 (19,datetime.date(2022,1,1),datetime.date(2023,1,1),"National Gallery (London)"),
                 (20,datetime.date(2023,1,1),datetime.date(2024,1,1),"National Gallery (London)"),
                 (21,datetime.date(2023,1,1),datetime.date(2024,1,1),"National Gallery (London)")]

    galleries =[("Louvre",),("British Museum",),("Museo del Prado",),
            ("National Gallery (London)",)]

    artists = [
        (1,"Leonardo","Da Vinci","Italian","Leonardo di ser Piero da Vinci(15 April 1452 – 2 May 1519) was an Italian polymath of the High Renaissance who was active as a painter, draughtsman, engineer, scientist, theorist, sculptor, and architect.While his fame initially rested on his achievements as a painter, he also became known for his notebooks, in which he made drawings and notes on a variety of subjects, including anatomy, astronomy, botany, cartography, painting, and paleontology. Leonardo is widely regarded to have been a genius who epitomized the Renaissance humanist ideal,[4] and his collective works comprise a contribution to later generations of artists matched only by that of his younger contemporary, Michelangelo."),
        (2,"Claude","Monet","French","Oscar-Claude Monet (UK: /ˈmɒneɪ/, US: /moʊˈneɪ, məˈ-/, French: [klod mɔnɛ]; 14 November 1840 – 5 December 1926) was a French painter and founder of impressionist painting who is seen as a key precursor to modernism, especially in his attempts to paint nature as he perceived it.[1] During his long career, he was the most consistent and prolific practitioner of impressionism's philosophy of expressing one's perceptions before nature, especially as applied to plein air (outdoor) landscape painting.[2] The term Impressionism is derived from the title of his painting Impression, soleil levant, exhibited in 1874 (the exhibition of rejects) initiated by Monet and his associates as an alternative to the Salon."),
        (3,"Vincent","Van Gogh", "Dutch","Vincent Willem van Gogh (Dutch: [ˈvɪnsɛnt ˈʋɪləm vɑŋ ˈɣɔx] (listen);[note 1] 30 March 1853 – 29 July 1890) was a Dutch Post-Impressionist painter who posthumously became one of the most famous and influential figures in Western art history. In a decade, he created about 2,100 artworks, including around 860 oil paintings, most of which date from the last two years of his life. They include landscapes, still lifes, portraits and self-portraits, and are characterised by bold colours and dramatic, impulsive and expressive brushwork that contributed to the foundations of modern art. Not commercially successful in his career, he struggled with severe depression and poverty, which eventually led to his suicide at age thirty-seven."),
        (4,"Jackson","Pollock","American","Paul Jackson Pollock (/ˈpɒlək/; January 28, 1912 – August 11, 1956) was an American painter and a major figure in the abstract expressionist movement. He was widely noticed for his drip technique of pouring or splashing liquid household paint onto a horizontal surface, enabling him to view and paint his canvases from all angles. It was called all-over painting and action painting, since he covered the entire canvas and used the force of his whole body to paint, often in a frenetic dancing style. This extreme form of abstraction divided the critics: some praised the immediacy of the creation, while others derided the random effects. In 2016, Pollock's painting titled Number 17A was reported to have fetched US$200 million in a private purchase."),
        (5,"Domenikos","Theotokopoulos","Greek","Domḗnikos Theotokópoulos (Greek: Δομήνικος Θεοτοκόπουλος, IPA: [ðoˈminikos θeotoˈkopulos]; 1 October 1541 – 7 April 1614),[2] most widely known as El Greco (Spanish pronunciation: [el ˈɣɾeko]; The Greek), was a Greek painter, sculptor and architect of the Spanish Renaissance. El Greco was a nickname,[a] and the artist normally signed his paintings with his full birth name in Greek letters, often adding the word Κρής (Krḗs), which means CretanEl Greco was born in the Kingdom of Candia (modern Crete), which was at that time part of the Republic of Venice, Italy, and the center of Post-Byzantine art. He trained and became a master within that tradition before traveling at age 26 to Venice, as other Greek artists had done.[6] In 1570, he moved to Rome, where he opened a workshop and executed a series of works. During his stay in Italy, El Greco enriched his style with elements of Mannerism and of the Venetian Renaissance taken from a number of great artists of the time, notably Tintoretto. In 1577, he moved to Toledo, Spain, where he lived and worked until his death. In Toledo, El Greco received several major commissions and produced his best-known paintings, such as View of Toledo and Opening of the Fifth Seal."),
        (6,"Jan","van Eyck","Dutch","Jan van Eyck (/væn ˈaɪk/ van EYEK, Dutch: [ˈjɑn vɑn ˈɛik]; c. before 1390 – 9 July 1441) was a painter active in Bruges who was one of the early innovators of what became known as Early Netherlandish painting, and one of the most significant representatives of Early Northern Renaissance art. According to Vasari and other art historians including Ernst Gombrich, he invented oil painting,[1] though most now regard that claim as an oversimplification."),
        (7,"Eugene","Delacroix","French","Ferdinand Victor Eugène Delacroix (/ˈdɛləkrwɑː, ˌdɛləˈkrwɑː/ DEL-ə-krwah, -⁠KRWAH,[1] French: [øʒɛn dəlakʁwa]; 26 April 1798 – 13 August 1863) was a French Romantic artist regarded from the outset of his career as the leader of the French Romantic school.[2]"),
        (8,"Andrea","del Verrochio","Italian","Andrea del Verrocchio (/vəˈroʊkioʊ/,[1][2] US also /-ˈrɔːk-/,[3] Italian: [anˈdrɛːa del verˈrɔkkjo]; c. 1435 – 1488), born Andrea di Michele di Francesco de' Cioni, was a sculptor, Italian painter and goldsmith who was a master of an important workshop in Florence. He apparently became known as Verrocchio after the surname of his master, a goldsmith. Few paintings are attributed to him with certainty, but a number of important painters were trained at his workshop. His pupils included Leonardo da Vinci, Pietro Perugino and Lorenzo di Credi. His greatest importance was as a sculptor and his last work, the Equestrian statue of Bartolomeo Colleoni in Venice, is generally accepted as a masterpiece."),
        (9,"Nikos", "Eggonopoylos","Greek","Nikos Egonopoulos was born in Athens in 1907 and was the second son of Panaghiotis and Errietti (Henrietta) Egonopoulos. During the summer of 1914, when Egonopoulos' family went on a trip to Constantinople, the family were obliged to settle there, due to the outbreak of World War I. In 1923, he was enrolled in a lycée in Paris, where he studied for a period of four years. After his return to Greece, he served as a private in the 1st Infantry Regiment."),
        (10,"Nikiforos","Lytras","Greek","Nikiforos Lytras (Greek: Νικηφόρος Λύτρας; 1832 – 13 June 1904) was a Greek painter. He was born in Tinos and trained in Athens at the School of Arts. In 1860, he won a scholarship to Royal Academy of Fine Arts of Munich. After completing these studies, he became a professor at the School of Arts in 1866, a position he held for the rest of his life. He remained faithful to the precepts and principles of the Munich School, while paying greatest attention both to ethnographic themes and portraiture. His most famous portrait was of the royal couple, Otto and Amalia, and his most well-known landscape a depiction of the region of Lavrio.")
        ]



    paintings=[
	(1,"Mona Lisa",1503,"Rennaisance",1),
        (2,"Lady with an Ermine",1489,"Rennaisance",1),
	(3,"Starry Night",1889,"Impressionism",3),
	(4,"The Potato Eaters",1885,"Impressionism",3),
	(5,"Van Gogh self-portrait",1889,"Impressionism",3),
	(6,"Liberty Leading the People",1830,"Romanticism",7),
	(7,"The Massacre at Chios",1824,"Romanticism",7),
	(8,"Wild Poppies",1873,"Impressionism",2),
	(9,"Impression, Sunrise",1873,"Impressionism",2),
	(10,"Convergence",1952,"Modern",4),
	(11,"Mural",1943,"Modern",4),
        (12,"The Disrobing of Christ",1579,"Rennaisance",5),
	(13,"The Adoration of the Shepherds",1614,"Rennaisance",5),
        (14,"Madonna of Chancellor Rolin",1435,"Rennaisance",6),
        (15,"Antique warrior in profile",1472,"Rennaisance",1),
        (16,"Virgin and Child with Two Angels",1478,"Rennaisance",8),
        (17,"Adoration of the Child",1484,"Rennaisance",8),
        (18,"Tobias and the Angel",1480,"Rennaisance",8),
        (19,"Gamos",1957,"Modern",9),
        (20,"Odisseys kai kalypso",1956,"Modern",9),
        (21,"O Galatas",1895,"Modern",10),
        ]


    conn.executemany("INSERT INTO Painting VALUES (?,?,?,?,?)",paintings)#Insert from a list of tuples
    conn.executemany("INSERT INTO Artist VALUES (?,?,?,?,?)",artists)
    conn.executemany("INSERT INTO Associate_Gallery VALUES (?)",galleries)
    conn.executemany("INSERT INTO Owned VALUES (?)",Idioktitos)
    conn.executemany("INSERT INTO Loan VALUES (?,?,?,?)",loanedpaintings)
    conn.executemany("INSERT INTO Takes VALUES (?,?,?,?)",loanedto)
 
    conn.commit()
    print("Data Inserted Succesfully\n")



def createdatabase():
    global conn
    conn=sqlite3.connect("art.sqlite") # table definitions
    table1="""CREATE TABLE Painting ( 
	artid INTEGER ,
	Title varchar NOT NULL,
	Creationyear INTEGER,
	ArtPeriod_name varchar,
	ArtistID integer,
	PRIMARY KEY (artid),
	FOREIGN KEY (ArtistID) REFERENCES Artist(ID)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE
);"""
    table2="""CREATE TABLE Artist (
	ID INTEGER ,
	Name varchar NOT NULL,
	Surname varchar,
	Nationality varchar,
	Description varchar,
	PRIMARY KEY (ID) 
);"""

    table3="""CREATE TABLE Associate_Gallery (
	Name varchar, 
	PRIMARY KEY (Name)
);"""
    table4="""CREATE TABLE Owned (
	artid integer,
	PRIMARY KEY(artid),
	FOREIGN KEY (artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE
);
"""
    table5="""CREATE TABLE Loan (
	artid integer,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	OriginName varchar NOT NULL,
	PRIMARY KEY (artid),
	FOREIGN KEY(artid) REFERENCES Painting(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (OriginName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
	
);"""
    table6="""CREATE TABLE Takes (
	artid integer ,
	BorrowerName VARCHAR,
	LoanStart date NOT NULL,
	LoanEnd date NOT NULL,
	PRIMARY KEY (artid, BorrowerName),
	FOREIGN KEY (artid) REFERENCES Owned(artid)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	FOREIGN KEY (BorrowerName) REFERENCES Associate_Gallery(Name)
	ON	DELETE	CASCADE		ON	UPDATE		CASCADE,
	CONSTRAINT dates CHECK (LoanStart<LoanEnd)
);"""

    conn.execute(table1) #table creations
    conn.execute(table2)
    conn.execute(table3)
    conn.execute(table4)
    conn.execute(table5)
    conn.execute(table6)

    print("Art Museum DataBase Succesfully Created")
  
    
if __name__=="__main__":
    createdatabase()
    load_data()
