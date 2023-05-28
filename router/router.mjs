import express from 'express';

import multer from 'multer';

const router = express.Router();
const controller =await import('../controller/controller.mjs');

const storage = multer.diskStorage({
    destination: './public/img/', // Replace with the specific folder path you want to save the file to
    filename: function (req, file, cb) {
      cb(null, file.originalname); // Use the original filename
    }
  });
const upload = multer({ storage });

router.route('/').get( (req, res) => {res.redirect('/home');});
router.route('/home').get(controller.showHome);
router.route('/login').get(controller.showLogin).post(controller.Login);
router.route('/collabs').get(controller.showCollabs);
router.route('/logout').get(controller.Logout);
router.get('/collect', controller.showCollection);
router.get('/artists', controller.showArtist);
router.get('/perma', controller.showPermanent);
router.get('/temp', controller.showTemp);
router.get('/archive', controller.showArchive);

router.post('/createArtist', controller.createArtist);
router.post('/createArt', controller.createArt);

router.get('/upload', (req, res) => {
    res.render('upload'); // Render your upload form template
  });
// Route to handle the file upload
router.post('/upload', upload.single('image'), (req, res) => {
    // Handle the uploaded file here
    console.log(req.file); // Access the uploaded file information
  
    // Redirect or render a success page
    res.redirect('/collect');
  });

router.post('/CollabUpload', upload.single('image'), (req, res) => {
    // Handle the uploaded file here
    console.log(req.file); // Access the uploaded file information

    // Redirect or render a success page
    res.redirect('/collabs');
  });
  
router.get('/deleteArt', (req,res) => {
    res.render('deleteArt');
});
router.post('/deleteArt', controller.deleteArt); // Delete art from collection

router.get('/deleteArtist', (req,res) => {
    res.render('deleteArtist');
});

router.post('/deleteArtist', controller.deleteArtist); // Delete artist from collection
router.get('/deleteCollab', (req,res) => {
    res.render('deleteCollab');
});
router.post('/deleteCollab', controller.deleteCollab); // Delete collab from collection

router.post('/createCollab', controller.createCollab); // Create collab

router.get('/upload', (req, res) => {
  res.render('upload'); // Render your upload form template
});
// Route to handle the file upload
router.post('/upload', upload.single('image'), (req, res) => {
  // Handle the uploaded file here
  console.log(req.file); // Access the uploaded file information

  // Redirect or render a success page
  res.redirect('/collabs');
});



export default router;
