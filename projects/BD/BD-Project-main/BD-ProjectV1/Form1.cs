using System.Data;
using System.Text;
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

            // Hide all empresa-related elements initially
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
            listBox1.Visible = true;
            EmpresaNome.Visible = true;
            EmpresaNIF.Visible = true;
            EmpresaEndereco.Visible = true;
            EmpresaTelefone.Visible = true;
            EmpresaEmail.Visible = true;
            EmpresaAdicionar.Visible = true;
            label1.Visible = true;
            label2.Visible = true;
            label3.Visible = true;
            label4.Visible = true;
            label5.Visible = true;
            EmpresaApagar.Visible = true;
            EmpresaEditar.Visible = true;

            SqlCommand cmd = new SqlCommand("SELECT * FROM GP_Empresa;", cn);
            SqlDataReader reader = cmd.ExecuteReader();

            listBox1.Items.Clear();

            while (reader.Read())
            {
                string nome = reader["Nome"].ToString();
                string nif = reader["NIF"].ToString();
                string endereco = reader["Endereco"].ToString();
                string telefone = reader["Telefone"].ToString();
                string email = reader["Email"].ToString();

                listBox1.Items.Add($"{nome} | {nif} |{endereco} | {telefone} | {email}");
            }

            reader.Close();
        }


        private void AddEmpresaButton_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            string nome = EmpresaNome.Text;
            string nif = EmpresaNIF.Text;
            string endereco = EmpresaEndereco.Text;
            string telefone = EmpresaTelefone.Text;
            string email = EmpresaEmail.Text;

            if (string.IsNullOrWhiteSpace(nome) || string.IsNullOrWhiteSpace(email))
            {
                MessageBox.Show("Nome e Email são obrigatórios.");
                return;
            }

            SqlCommand cmd = new SqlCommand("INSERT INTO GP_Empresa (NIF, Nome, Endereco, Telefone, Email) VALUES (@nif, @nome, @endereco, @telefone, @email);", cn);
            cmd.Parameters.AddWithValue("@nome", nome);
            cmd.Parameters.AddWithValue("@nif", nif);
            cmd.Parameters.AddWithValue("@endereco", endereco);
            cmd.Parameters.AddWithValue("@telefone", telefone);
            cmd.Parameters.AddWithValue("@email", email);

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Empresa adicionada com sucesso!");
                    ShowEmpresasButton_Click(null, null); // Atualizar lista
                }
                else
                {
                    MessageBox.Show("Erro ao adicionar empresa.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        }

        private void EmpresaApagar_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa para apagar.");
                return;
            }

            string selectedLine = listBox1.SelectedItem.ToString();
            // Supondo que os campos estão no formato: Nome | NIF | Endereço | Telefone | Email
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string nif = parts[1].Trim();

            DialogResult result = MessageBox.Show($"Tem a certeza que deseja apagar a empresa com NIF {nif}?", "Confirmar Apagar", MessageBoxButtons.YesNo);
            if (result != DialogResult.Yes)
                return;

            SqlCommand cmd = new SqlCommand("DELETE FROM GP_Empresa WHERE NIF = @nif;", cn);
            cmd.Parameters.AddWithValue("@nif", nif);

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Empresa apagada com sucesso!");
                    ShowEmpresasButton_Click(null, null); // Atualizar lista
                }
                else
                {
                    MessageBox.Show("Erro: Empresa não encontrada.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao apagar: " + ex.Message);
            }
        }

        private void EmpresaEditar_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa primeiro.");
                return;
            }

            string nif = EmpresaNIF.Text.Trim();
            string nome = EmpresaNome.Text.Trim();
            string endereco = EmpresaEndereco.Text.Trim();
            string telefone = EmpresaTelefone.Text.Trim();
            string email = EmpresaEmail.Text.Trim();

            if (string.IsNullOrWhiteSpace(nome) || string.IsNullOrWhiteSpace(email))
            {
                MessageBox.Show("Nome e Email são obrigatórios.");
                return;
            }

            SqlCommand cmd = new SqlCommand(
                "UPDATE GP_Empresa SET Nome=@nome, Endereco=@endereco, Telefone=@telefone, Email=@email WHERE NIF=@nif;", cn);

            cmd.Parameters.AddWithValue("@nif", nif);
            cmd.Parameters.AddWithValue("@nome", nome);
            cmd.Parameters.AddWithValue("@endereco", endereco);
            cmd.Parameters.AddWithValue("@telefone", telefone);
            cmd.Parameters.AddWithValue("@email", email);

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Empresa atualizada com sucesso!");
                    ShowEmpresasButton_Click(null, null); // Atualiza lista
                }
                else
                {
                    MessageBox.Show("Erro: Empresa não encontrada.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao atualizar: " + ex.Message);
            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
                return;

            string selectedLine = listBox1.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 5)
            {
                MessageBox.Show("Erro ao analisar a empresa selecionada.");
                return;
            }

            EmpresaNome.Text = parts[0].Trim();
            EmpresaNIF.Text = parts[1].Trim();
            EmpresaEndereco.Text = parts[2].Trim();
            EmpresaTelefone.Text = parts[3].Trim();
            EmpresaEmail.Text = parts[4].Trim();

            EmpresaNIF.Enabled = false;
        }

        private void SearchBy_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void NavioShow_Click(object sender, EventArgs e)
        {
            Form2 newForm = new Form2();
            newForm.Show();
        }

        private void EmpresaSearch_TextChanged(object sender, EventArgs e)
        {

        }

        private void Apply_Click(object sender, EventArgs e)
        {
            if (!verifySGBDConnection())
                return;

            string searchTerm = EmpresaSearch.Text.Trim();
            string searchBy = SearchBy.SelectedItem?.ToString();
            string sortBy = comboBox1.SelectedItem?.ToString();
            string sortOrder = sort.SelectedItem?.ToString();

            // Build the base query
            string query = "SELECT * FROM GP_Empresa";

            // Add WHERE clause if search criteria are specified
            if (!string.IsNullOrWhiteSpace(searchTerm) && searchBy != "---" && searchBy != null)
            {
                query += " WHERE ";
                switch (searchBy)
                {
                    case "Nome":
                        query += "Nome LIKE @searchTerm";
                        break;
                    case "NIF":
                        query += "NIF LIKE @searchTerm";
                        break;
                    case "Endereço":
                        query += "Endereco LIKE @searchTerm";
                        break;
                    case "Telefone":
                        query += "Telefone LIKE @searchTerm";
                        break;
                    case "Email":
                        query += "Email LIKE @searchTerm";
                        break;
                }
            }

            // Add ORDER BY clause if sort criteria are specified
            if (!string.IsNullOrWhiteSpace(sortBy) && sortBy != "---" && !string.IsNullOrWhiteSpace(sortOrder))
            {
                query += " ORDER BY ";
                switch (sortBy)
                {
                    case "Nome":
                        query += "Nome";
                        break;
                    case "NIF":
                        query += "NIF";
                        break;
                    case "Endereço":
                        query += "Endereco";
                        break;
                    case "Telefone":
                        query += "Telefone";
                        break;
                    case "Email":
                        query += "Email";
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
                listBox1.Items.Clear();

                while (reader.Read())
                {
                    string nome = reader["Nome"].ToString();
                    string nif = reader["NIF"].ToString();
                    string endereco = reader["Endereco"].ToString();
                    string telefone = reader["Telefone"].ToString();
                    string email = reader["Email"].ToString();

                    listBox1.Items.Add($"{nome} | {nif} | {endereco} | {telefone} | {email}");
                }

                reader.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao pesquisar: " + ex.Message);
            }
        }

        private void ShowNaviosButton_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa primeiro.");
                return;
            }

            string selectedLine = listBox1.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string nif = parts[1].Trim();

            if (!verifySGBDConnection())
                return;

            try
            {
                SqlCommand cmd = new SqlCommand(
                    "SELECT Nome, Capacidade_Toneladas FROM GP_Navio WHERE NIF_Empresa = @nif;",
                    cn);
                cmd.Parameters.AddWithValue("@nif", nif);

                SqlDataReader reader = cmd.ExecuteReader();
                StringBuilder naviosInfo = new StringBuilder();
                naviosInfo.AppendLine($"Navios associados à empresa (NIF: {nif}):");
                naviosInfo.AppendLine("----------------------------------");

                bool hasNavios = false;
                while (reader.Read())
                {
                    hasNavios = true;
                    string nome = reader["Nome"].ToString();
                    string capacidade = reader["Capacidade_Toneladas"].ToString();
                    naviosInfo.AppendLine($"- {nome} (Capacidade: {capacidade} toneladas)");
                }

                reader.Close();

                if (!hasNavios)
                {
                    naviosInfo.AppendLine("Nenhum navio associado a esta empresa.");
                }

                MessageBox.Show(naviosInfo.ToString(), "Navios da Empresa");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao buscar navios: " + ex.Message);
            }
        }
    }
}
    
