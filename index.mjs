import express from 'express';
import { engine }from 'express-handlebars';
import router from './router/router.mjs'
import session from 'express-session';

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.static('public'));

app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: {maxAge: 600000 } // Adjust the maxAge value as desired (in milliseconds)
}));

// Χρήση του Handlebars ως view engine
app.engine('.hbs', engine({extname: '.hbs'}));
app.set('view engine', '.hbs');

//CODE FOR LOGIN
app.use((req, res, next) => {
  if (req.session.isLoggedIn) {
    // User is logged in
    res.locals.isLoggedIn = true;
    res.locals.username = req.session.username;
  } else {
    // User is not logged in
    res.locals.isLoggedIn = false;
    res.locals.username = null;
  }
  next();
});

// Αρχική σελίδα
app.use('/', router);

// CODE FOR LOGOUT
app.get('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.log('Error destroying session:', err);
    } else {
      res.redirect('/');
    }
  });
});



app.listen(port, () => {
  console.log(`http://localhost:${port}`);
});