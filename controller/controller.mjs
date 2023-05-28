const model = await import(`../model/model.mjs`);

export async function showHome(req,res) {
    try {
        res.render('home',{session: req.session});
    }
    catch (err) {
        console.log(err);
    }}

export async function showLogin(req,res) {
    try {
        res.render('login');
    }
    catch (err) {
        console.log(err);
    }}

    export async function showCollection(req,res) {
        try {
            const pain = await model.getAllPaintings();
            res.render('collect', { pain:pain});
        }
        catch (err) {
            console.log(err);
        }}

        export async function showCollabs(req,res) {
            try {
                const collabs = await model.getAllCollabs();   
                res.render('collabs', { collabs:collabs});
            }
            catch (err) {
                console.log(err);
            }}

export async function Login(req,res) {
    if (req.body.username == "admin" && req.body.password == "admin") {
        req.session.isLoggedIn = true;
        res.redirect("/home");
    } else {
         res.locals.errorMessage = "Incorrect username or password";
         res.render("login");
    }};

export async function Logout(req,res) {
    req.session.destroy((err) => {
        if (err) {
            console.log('Error destroying session:', err);
        } else {
            res.redirect('/');
        }
    });}

    export async function showArtist(req,res) {
        try {
            const artist = await model.getAllArtist();   
            res.render('artists', {artist:artist});
        }
        catch (err) {
            console.log(err);
        }}

        export async function showPermanent(req,res) {
            try {
                const perma = await model.getPermanent();
                res.render('perma', { perma:perma});
            }
            catch (err) {
                console.log(err);
            }}

        export async function showTemp(req,res) {
            try {
                const temp = await model.getTemporary();
                res.render('temp', { temp:temp});
            }
            catch (err) {
                console.log(err);
            }}
export async function showArchive(req,res) {
    try {
        const archive = await model.getArchive();
        res.render('archive', { archive:archive});
    }
    catch (err) {
        console.log(err);
    }}




export async function createArtist(req, res) {
    await model.createArtist(req.body.Name, req.body.Surname, req.body.Nationality, req.body.Description);
    res.redirect('/artists');
}

export async function createArt(req, res) {
    await model.createArt(req.body.Title, req.body.Creationyear, req.body.ArtPeriod_name, req.body.Name, req.body.Surname, req.body.Temp, req.body.LoanStart, req.body.LoanEnd ,req.body.OriginName );
    res.redirect('/collect');
}

export async function deleteArt(req, res) {
    await model.deleteArt(req.body.Title);
    res.redirect('/collect');
}   

export async function deleteArtist(req, res) {
    await model.deleteArtist(req.body.Name, req.body.Surname);
    res.redirect('/artists');
}

export async function deleteCollab(req, res) {
    await model.deleteCollab(req.body.Name);
    res.redirect('/collabs');
}
export async function createCollab(req, res) {
    await model.createCollab(req.body.Name);
    res.redirect('/collabs');
}