using System.Data;
using System.Globalization;
using System.Text;
using System.Windows.Forms;
using Microsoft.Data.SqlClient; 

namespace BD_Final_Project
{
    public partial class EmpresasPanel : UserControl
    {
        public EmpresasPanel()
        {
            InitializeComponent();
        }

        private void EmpresasPanel_Load(object sender, EventArgs e)
        {
        }

        private SqlConnection cn;

        public void SetConnection(SqlConnection connection)
        {
            cn = connection;
        }

        public void LoadEmpresas()
        {
            listBoxEmpresas.Items.Clear();
            panel1.Visible = true;

            SqlCommand cmd = new SqlCommand("SelectAllEmpresas", cn);
            SqlDataReader reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                string nome = reader["Nome"].ToString();
                string nif = reader["NIF"].ToString();
                string endereco = reader["Endereco"].ToString();
                string telefone = reader["Telefone"].ToString();
                string email = reader["Email"].ToString();

                listBoxEmpresas.Items.Add($"{nome} | {nif} | {endereco} | {telefone} | {email}");
            }

            reader.Close();
        }

        private void AddEmpresaButton_Click(object sender, EventArgs e)
        {
            if (cn == null || cn.State != ConnectionState.Open)
            {
                MessageBox.Show("Sem ligação à base de dados.");
                return;
            }

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

            try
            {
                using (SqlCommand cmd = new SqlCommand("AddEmpresa", cn))
                {
                    cmd.CommandType = CommandType.StoredProcedure;

                    // Add parameters
                    cmd.Parameters.Add("@Nome", SqlDbType.VarChar, 100).Value = nome;
                    cmd.Parameters.Add("@NIF", SqlDbType.Char, 9).Value = nif;
                    cmd.Parameters.Add("@Endereco", SqlDbType.VarChar, 200).Value = endereco;
                    cmd.Parameters.Add("@Telefone", SqlDbType.VarChar, 20).Value = telefone;
                    cmd.Parameters.Add("@Email", SqlDbType.VarChar, 100).Value = email;

                    // Add return value parameter
                    cmd.Parameters.Add("@ReturnValue", SqlDbType.Int).Direction = ParameterDirection.ReturnValue;

                    cmd.ExecuteNonQuery();

                    int rowsAffected = (int)cmd.Parameters["@ReturnValue"].Value;

                    if (rowsAffected > 0)
                    {
                        MessageBox.Show("Empresa adicionada com sucesso!");
                        LoadEmpresas();
                    }
                    else
                    {
                        MessageBox.Show("Erro ao adicionar empresa.");
                    }
                }
            }
            catch (SqlException ex)
            {
                MessageBox.Show("Erro de base de dados: " + ex.Message);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro: " + ex.Message);
            }
        }

        private void EmpresaApagar_Click(object sender, EventArgs e)
        {
            if (listBoxEmpresas.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa para apagar.");
                return;
            }

            string selectedLine = listBoxEmpresas.SelectedItem.ToString();
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

            SqlCommand cmd = new SqlCommand();
            cmd.CommandText = "EXEC dbo.DeleteEmpresa @NIF=@NIF";
            cmd.Parameters.AddWithValue("@NIF", nif);
            cmd.Connection = cn;


            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Empresa apagada com sucesso!");
                    LoadEmpresas();
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
            if (listBoxEmpresas.SelectedItem == null)
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

            SqlCommand cmd = new SqlCommand();
            cmd.CommandText = "EXEC dbo.UpdateEmpresa @Nome=@nome, @Endereco=@endereco, @Telefone=@telefone, @Email=@email, @NIF=@nif";
            cmd.Parameters.AddWithValue("@nif", nif);
            cmd.Parameters.AddWithValue("@nome", nome);
            cmd.Parameters.AddWithValue("@endereco", endereco);
            cmd.Parameters.AddWithValue("@telefone", telefone);
            cmd.Parameters.AddWithValue("@email", email);
            cmd.Connection = cn;

            try
            {
                // Adiciona parâmetro de retorno
                SqlParameter returnParam = cmd.Parameters.Add("@ReturnVal", SqlDbType.Int);
                returnParam.Direction = ParameterDirection.ReturnValue;

                cmd.ExecuteNonQuery();

                int rowsAffected = (int)returnParam.Value;

                if (rowsAffected == 0)
                {
                    MessageBox.Show("Empresa atualizada com sucesso!");
                    LoadEmpresas();
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

        private void listBoxEmpresas_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBoxEmpresas.SelectedItem == null)
                return;

            string selectedLine = listBoxEmpresas.SelectedItem.ToString();
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
        }

        private void Apply_Click(object sender, EventArgs e)
        {
            if (cn == null || cn.State != ConnectionState.Open)
            {
                MessageBox.Show("Sem ligação à base de dados.");
                return;
            }

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
                listBoxEmpresas.Items.Clear();

                while (reader.Read())
                {
                    string nome = reader["Nome"].ToString();
                    string nif = reader["NIF"].ToString();
                    string endereco = reader["Endereco"].ToString();
                    string telefone = reader["Telefone"].ToString();
                    string email = reader["Email"].ToString();

                    listBoxEmpresas.Items.Add($"{nome} | {nif} | {endereco} | {telefone} | {email}");
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
            if (listBoxEmpresas.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa primeiro.");
                return;
            }

            string selectedLine = listBoxEmpresas.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string nif = parts[1].Trim();

            if (cn == null || cn.State != ConnectionState.Open)
            {
                MessageBox.Show("Sem ligação à base de dados.");
                return;
            }

            try
            {
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = "EXEC dbo.GetNaviosByEmpresa @NIF=@NIF";
                cmd.Parameters.AddWithValue("@NIF", nif);
                cmd.Connection = cn;

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

        public event EventHandler<string> NavioAdicionarRequested;

        public void NavioAdicionar_Click(object sender, EventArgs e)
        {
            if (listBoxEmpresas.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa primeiro.");
                return;
            }

            // Podes também extrair o NIF se precisares de o passar a outro painel/formulário:
            string selectedLine = listBoxEmpresas.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string nif = parts[1].Trim();

            // Raise the event to notify the parent form
            NavioAdicionarRequested?.Invoke(this, nif);
        }
    }
}
