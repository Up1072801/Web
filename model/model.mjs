'use strict';
// Το sqlite-async χρησιμοποιεί το ίδιο API όπως και το sqlite3, αλλά με promises
import { Database } from 'sqlite-async';

let sql;
try {
    sql = await Database.open('model/art.sqlite')
} catch (error) {
    throw Error('Δεν ήταν δυνατό να ανοίξει η βάση δεδομένων.' + error);
}

export let getAllPaintings = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("SELECT Painting.artid, Painting.Title, Painting.Creationyear, Painting.Artperiod_name, Artist.Name, Artist.Surname FROM Painting join Artist on Painting.ArtistID = Artist.ID"); 
        const pain = await stmt.all();
        return pain;
    } catch (err) {
        console.log(err);
    }
}

export let getAllCollabs = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("SELECT * from Associate_Gallery"); 
        const collabs = await stmt.all();
        return collabs;
    } catch (err) {
        console.log(err);
    }
}

export let getAllArtist = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("SELECT * from Artist order by Name"); 
        const artist = await stmt.all();
        return artist;
    } catch (err) {
        console.log(err);
    }
}

export let getPermanent = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("select Painting.artid, Title , Creationyear , ArtPeriod_name, Artist.Name , Artist.Surname from Painting join Artist on Painting.ArtistID = Artist.ID EXCEPT select Painting.artid, Title , Creationyear , ArtPeriod_name, Artist.Name , Artist.Surname from Takes join Painting on Painting.artid = Takes.artid join Artist on Painting.ArtistID = Artist.ID where Date(Takes.LoanEnd) < DATE() Except select Painting.artid, Title, Creationyear , Artperiod_name , Artist.Name , Artist.Surname from Loan join Painting on painting.artid = Loan.artid join Artist on Painting.ArtistID = Artist.ID"); 
        const perma = await stmt.all();
        return perma;
    } catch (err) {
        console.log(err);
    }
}

export let getTemporary = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("select Painting.artid , Painting.Title , Painting.Creationyear , Painting.ArtPeriod_name, Artist.Name , Artist.Surname from Loan join Painting on Painting.artid = Loan.artid join Artist on painting.ArtistID = Artist.ID where Date(Loan.LoanEnd) > DATE() ;"); 
        const temp = await stmt.all();
        return temp;
    } catch (err) {
        console.log(err);
    }
}

export let getArchive = async () => {
    try {
        //Φέρε όλες τις εργασίας από τη βάση
        const stmt = await sql.prepare("select Painting.artid , Painting.Title , Painting.Creationyear , Painting.ArtPeriod_name, Artist.Name , Artist.Surname from Loan join Painting on Painting.artid = Loan.artid join Artist on painting.ArtistID = Artist.ID where Date(Loan.LoanEnd) < DATE() ;"); 
        const ex = await stmt.all();
        return ex;
    } catch (err) {
        console.log(err);
    }
}

//function to insert new artist
export async function createArtist(Name,Surname,Nationality,Description) {
    try{
    //Φτιάξε το query που θα κάνει την εισαγωγή
    const stmt = await sql.prepare("INSERT INTO Artist (Name, Surname, Nationality, Description) VALUES (?, ?, ?, ?)");
    //Κάνε την εισαγωγή
    await stmt.run(Name, Surname, Nationality, Description);
    //Αν υπάρχει κάποιο σφάλμα, επέστρεψε το
    } catch (err) {
        console.log(err);
    }
}

//function to insert new art
export async function createArt(Title,Creationyear,ArtPeriod_name,Name,Surname,Temp , LoanStart, LoanEnd , OriginName) {
    try{
    //Φτιάξε το query που θα κάνει την εισαγωγή
    const new_stmt = await sql.prepare("Select ID from Artist where Name = ? AND Surname = ? ");
    const ArtistID = await new_stmt.get(Name,Surname);
    const stmt = await sql.prepare("INSERT INTO Painting (Title, Creationyear, ArtPeriod_name, ArtistID) VALUES (?, ?, ?, ?)");
    await stmt.run(Title, Creationyear, ArtPeriod_name, ArtistID.ID);
    const artid = await sql.prepare("Select artid from Painting where Title = ? ");
    const ArtID = await artid.get(Title);
    if (Temp == "Temporary"){
        const stmt2 = await sql.prepare("INSERT INTO Loan (ArtID, LoanStart, LoanEnd, OriginName) VALUES (?, ?, ?, ?)");
        await stmt2.run(ArtID.artid, LoanStart,LoanEnd,OriginName);
    }
    //Κάνε την εισαγωγή
    
    
    //Αν υπάρχει κάποιο σφάλμα, επέστρεψε το
    } catch (err) {
        console.log(err);
    }
}


export async function deleteArt(Title) {
    try{
        const stmt = await sql.prepare("DELETE FROM painting where Title=? ");
        await stmt.run(Title);
    }
    catch(err){
        throw err;
    }
}
export async function deleteArtist(Name,Surname) { 
    try{
        const stmt = await sql.prepare("DELETE FROM Artist where Name=? AND Surname=? ");
        await stmt.run(Name,Surname);
    }
    catch(err){
        throw err;
    }
}
export async function deleteCollab(Name) {  
    try{
        const stmt = await sql.prepare("DELETE FROM Associate_Gallery where Name=? ");
        await stmt.run(Name);
    }
    catch(err){
        throw err;
    }
}
export async function createCollab(Name){
    try{
        const stmt = await sql.prepare("INSERT INTO Associate_Gallery (Name) VALUES (?)");
        await stmt.run(Name);
    }
    catch(err){
        throw err;
    }
} 

