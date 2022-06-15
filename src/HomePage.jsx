import * as React from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import ImgLogo from './login.png';
import Paper from '@mui/material/Paper';

function HomePage() {
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };
 
  return (

      <Container component="main" maxWidth="xs">
        <Paper elevation={15} 
        sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            padding: 3,
          }} >
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>

          <img src={ImgLogo} alt="logo" />

          <Typography component="h1" variant="h6">
            Connectez vous a votre compte ONA
          </Typography>
          <Box component="form"   onSubmit={handleSubmit} sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Adresse e-mail ou numéro de tél."
              name="email"
              autoComplete="email"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Mot de passe"
              type="password"
              id="password"
              autoComplete="current-password"
            />

            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Se souvenir de moi"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{'&:hover': {  
                backgroundColor: 'rgba(16, 127, 190, 0.842)',
                // eslint-disable-next-line no-dupe-keys
                backgroundColor: 'rgb(4, 28, 41)',},
                mt: 3,
                mb: 2, 
              }}
            >
              Se connecter
              
            </Button>
          </Box>
        </Box>
       </Paper>
      </Container>

  );
}
export default HomePage;