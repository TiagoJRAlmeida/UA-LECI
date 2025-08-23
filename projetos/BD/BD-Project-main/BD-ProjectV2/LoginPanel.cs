using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using Microsoft.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Security.Cryptography;

namespace BD_Final_Project
{
    public partial class LoginPanel : UserControl
    {
        public LoginPanel()
        {
            InitializeComponent();
        }

        private SqlConnection cn;

        public void SetConnection(SqlConnection connection)
        {
            cn = connection;
        }

        public event EventHandler LoggedIn;

        private void SignIn_Click(object sender, EventArgs e)
        {
            string username = textBox1.Text.Trim();
            string password = textBox2.Text;

            if (string.IsNullOrWhiteSpace(username) || string.IsNullOrWhiteSpace(password))
            {
                MessageBox.Show("Por favor, preencha todos os campos.");
                return;
            }

            using var sha256 = SHA256.Create();
            byte[] hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
            string hash = Convert.ToBase64String(hashBytes);

            var cmd = new SqlCommand("SELECT COUNT(*) FROM Utilizadores WHERE Username = @u AND PasswordHash = @p", cn);
            cmd.Parameters.AddWithValue("@u", username);
            cmd.Parameters.AddWithValue("@p", hash);

            int count = (int)cmd.ExecuteScalar();

            if (count > 0)
            {
                MessageBox.Show("Login bem-sucedido!");
                LoggedIn?.Invoke(this, EventArgs.Empty);
            }
            else
            {
                MessageBox.Show("Utilizador ou palavra-passe incorretos.");
            }
        }


        private void SignUp_Click(object sender, EventArgs e)
        {
            string username = textBox1.Text.Trim();
            string password = textBox2.Text;

            if (string.IsNullOrWhiteSpace(username) || string.IsNullOrWhiteSpace(password))
            {
                MessageBox.Show("Por favor, preencha todos os campos.");
                return;
            }

            using var sha256 = SHA256.Create();
            byte[] hashBytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
            string hash = Convert.ToBase64String(hashBytes);


            var checkCmd = new SqlCommand("SELECT COUNT(*) FROM Utilizadores WHERE Username = @u", cn);
            checkCmd.Parameters.AddWithValue("@u", username);
            int exists = (int)checkCmd.ExecuteScalar();

            if (exists > 0)
            {
                MessageBox.Show("Nome de utilizador já existe.");
                return;
            }

            var insertCmd = new SqlCommand("INSERT INTO Utilizadores (Username, PasswordHash) VALUES (@u, @p)", cn);
            insertCmd.Parameters.AddWithValue("@u", username);
            insertCmd.Parameters.AddWithValue("@p", hash);
            insertCmd.ExecuteNonQuery();

            MessageBox.Show("Registo efetuado com sucesso!");
        }
    }
}
