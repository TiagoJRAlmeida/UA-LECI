using System.Data;
using Microsoft.Data.SqlClient;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;

namespace BD_Final_Project
{
    public partial class Form2 : Form
    {
        private SqlConnection cn;
        public Form2()
        {
            InitializeComponent();
        }
        private void Form2_Load(object sender, EventArgs e)
        {



        }

        private SqlConnection getSGBDConnection()
        {
            return new SqlConnection("data source=mednat.ieeta.pt\\SQLSERVER,8101;initial catalog=p10g4;user id=p10g4;password='rP$v{!DS^thf-k;';TrustServerCertificate=True");
        }

        private bool verifySGBDConnection()
        {
            if (cn == null)
                cn = getSGBDConnection();

            if (cn.State != ConnectionState.Open)
                try
                {
                    cn.Open();

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Can not open connection!");
                    MessageBox.Show(ex.Message);
                }

            return cn.State == ConnectionState.Open;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void NavioShow_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            // Show navio-related elements

            SqlCommand cmd = new SqlCommand("SELECT * FROM GP_Navio;", cn);
            SqlDataReader reader = cmd.ExecuteReader();

            listBox2.Items.Clear();

            while (reader.Read())
            {
                string id = reader["ID"].ToString();
                string nome = reader["Nome"].ToString();
                string cap = reader["Capacidade_Toneladas"].ToString();
                string nif = reader["NIF_Empresa"].ToString();

                listBox2.Items.Add($"{id} | {nome} |{cap} | {nif}");
            }

            reader.Close();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Apply_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            string searchTerm = SearchBox.Text.Trim();
            string searchBy = comboBox1.SelectedItem?.ToString();
            string sortBy = comboBox2.SelectedItem?.ToString();
            string sortOrder = sort.SelectedItem?.ToString();

            // Build the base query
            string query = "SELECT * FROM GP_Navio";

            // Add WHERE clause if search criteria are specified
            if (!string.IsNullOrWhiteSpace(searchTerm) && searchBy != "---" && searchBy != null)
            {
                query += " WHERE ";
                switch (searchBy)
                {
                    case "ID":
                        query += "ID LIKE @searchTerm";
                        break;
                    case "Nome":
                        query += "Nome LIKE @searchTerm";
                        break;
                    case "Capacidade":
                        query += "Capacidade_Toneladas LIKE @searchTerm";
                        break;
                    case "NIF Empresa":
                        query += "NIF_Empresa LIKE @searchTerm";
                        break;
                }
            }

            // Add ORDER BY clause if sort criteria are specified
            if (!string.IsNullOrWhiteSpace(sortBy) && sortBy != "---" && !string.IsNullOrWhiteSpace(sortOrder))
            {
                query += " ORDER BY ";
                switch (sortBy)
                {
                    case "ID":
                        query += "ID";
                        break;
                    case "Nome":
                        query += "Nome";
                        break;
                    case "Capacidade (Toneladas)":
                        query += "Capacidade_Toneladas";
                        break;
                    case "NIF da Empresa":
                        query += "NIF_Empresa";
                        break;
                }

                query += sortOrder == "Decrescente" ? " DESC" : " ASC";
            }

            SqlCommand cmd = new SqlCommand(query, cn);

            if (!string.IsNullOrWhiteSpace(searchTerm) && searchBy != "---" && searchBy != null)
            {
                cmd.Parameters.AddWithValue("@searchTerm", "%" + searchTerm + "%");
            }

            try
            {
                SqlDataReader reader = cmd.ExecuteReader();
                listBox2.Items.Clear();

                while (reader.Read())
                {
                    string id = reader["ID"].ToString();
                    string nome = reader["Nome"].ToString();
                    string cap = reader["Capacidade_Toneladas"].ToString();
                    string nif = reader["NIF_Empresa"].ToString();

                    listBox2.Items.Add($"{id} | {nome} | {cap} | {nif}");
                }

                reader.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao pesquisar: " + ex.Message);
            }
        }

        private void AddNavio_Click(object sender, EventArgs e)
        {
            int id = int.Parse(NavioID.Text);
            float cap = float.Parse(NavioCapacidade.Text);
            string name = NavioNome.Text;
            string empresanif = NavioNIFEmpresa.Text;

            SqlCommand cmd = new SqlCommand("INSERT INTO GP_Navio VALUES (@id, @nome, @capacidade, @empresanif);", cn);
            cmd.Parameters.AddWithValue("@id", id);
            cmd.Parameters.AddWithValue("@nome", name);
            cmd.Parameters.AddWithValue("@capacidade", cap);
            cmd.Parameters.AddWithValue("@empresanif", empresanif);

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Navio adicionado com sucesso!");
                    NavioShow_Click(null, null); // Atualizar lista
                }
                else
                {
                    MessageBox.Show("Erro ao adicionar navio.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        }
    }
}
