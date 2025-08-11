using System.Data;
using Microsoft.Data.SqlClient;

namespace BD_Final_Project
{
    public partial class Form1 : Form
    {
        private SqlConnection cn;

        public Form1()
        {
            InitializeComponent();
        }
        
        private void Form1_Load(object sender, EventArgs e)
        {
            cn = getSGBDConnection();
            verifySGBDConnection();
            empresasPanel1.SetConnection(cn);
            naviosPanel1.SetConnection(cn);
            loginPanel1.SetConnection(cn);

            empresasPanel1.NavioAdicionarRequested += EmpresasPanel1_NavioAdicionarRequested;
            loginPanel1.LoggedIn += loginPanel1_LoggedIn;

            // Hide all elements initially

            empresasPanel1.Visible = false;
            naviosPanel1.Visible = false;
            loginPanel1.Visible = true;
        }

        private SqlConnection getSGBDConnection()
        {
            return new SqlConnection("data source=mednat.ieeta.pt\\SQLSERVER,8101;initial catalog=p10g4;user id=p10g4;password='rP$v{!DS^thf-k;';TrustServerCertificate=True");
        }

        public bool verifySGBDConnection()
        {
            if (cn == null)
                cn = getSGBDConnection();

            if (cn.State != ConnectionState.Open)
                try
                {
                    cn.Open();
                    MessageBox.Show("Connected!");
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Can not open connection!");
                    MessageBox.Show(ex.Message);
                }

            return cn.State == ConnectionState.Open;
        }

        private void ShowEmpresasButton_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            // Show empresa-related elements
            empresasPanel1.Visible = true;
            loginPanel1.Visible = false;
            naviosPanel1.Visible = false;
            empresasPanel1.LoadEmpresas();
        }

        private void ShowNaviosButton_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            // Show navios-related elements
            empresasPanel1.Visible = false;
            naviosPanel1.Visible = true;
            loginPanel1.Visible = false;
            naviosPanel1.LoadNavios();
        }

        private void EmpresasPanel1_NavioAdicionarRequested(object sender, String nif)
        {
            empresasPanel1.Visible = false;
            naviosPanel1.Visible = true;
            loginPanel1.Visible = false;
            naviosPanel1.LoadNavios();
            naviosPanel1.NavioEmpresaNIF.Text = nif;
        }

        private void loginPanel1_LoggedIn(object sender, EventArgs e)
        {
            empresasPanel1.Visible = true;
            naviosPanel1.Visible = false;
            loginPanel1.Visible = false;
            empresasPanel1.LoadEmpresas();
        }
    }
}
    
