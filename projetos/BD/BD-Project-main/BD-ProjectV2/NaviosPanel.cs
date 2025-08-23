using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Data.SqlClient;

namespace BD_Final_Project
{
    public partial class NaviosPanel : UserControl
    {
        public NaviosPanel()
        {
            InitializeComponent();
        }

        private SqlConnection cn;

        public void SetConnection(SqlConnection connection)
        {
            cn = connection;
        }

        private void NaviosPanel_Load(object sender, EventArgs e)
        {

        }

        public void LoadNavios()
        {
            listBoxNavios.Items.Clear();
            panel1.Visible = true;

            SqlCommand cmd = new SqlCommand("SELECT * FROM GP_Navio;", cn);
            SqlDataReader reader = cmd.ExecuteReader();

            while (reader.Read())
            {
                string id = reader["ID"].ToString();
                string nome = reader["Nome"].ToString();
                string capacidade_toneladas = reader["Capacidade_Toneladas"].ToString();
                string nif_empresa = reader["NIF_Empresa"].ToString();

                listBoxNavios.Items.Add($"{id} | {nome} | {capacidade_toneladas} | {nif_empresa}");
            }

            reader.Close();
        }

        private void NavioAdicionar_Click(object sender, EventArgs e)
        {
            if (cn == null || cn.State != ConnectionState.Open)
            {
                MessageBox.Show("Sem ligação à base de dados.");
                return;
            }
            string nome = NavioNome.Text;
            float capacidade;
            string nifEmpresa = NavioEmpresaNIF.Text;

            if (!float.TryParse(NavioCapacidade.Text, out capacidade))
            {
                MessageBox.Show("Capacidade inválida. Por favor insira um valor numérico.");
                return;
            }

            try
            {
                using (SqlCommand cmd = new SqlCommand("AddNavio", cn))
                {
                    cmd.CommandType = CommandType.StoredProcedure;

                    // Add parameters
                    cmd.Parameters.Add("@Nome", SqlDbType.VarChar, 100).Value = nome;
                    cmd.Parameters.Add("@Capacidade_Toneladas", SqlDbType.Float).Value = capacidade;
                    cmd.Parameters.Add("@NIF_Empresa", SqlDbType.Char, 9).Value = nifEmpresa;

                    // Adiciona parâmetro de retorno
                    SqlParameter returnParam = cmd.Parameters.Add("@ReturnVal", SqlDbType.Int);
                    returnParam.Direction = ParameterDirection.ReturnValue;

                    cmd.ExecuteNonQuery();

                    int rowsAffected = (int)returnParam.Value;

                    if (rowsAffected == 0)
                    {
                        MessageBox.Show("Navio adicionado com sucesso!");
                        LoadNavios();
                    }
                    else
                    {
                        MessageBox.Show("Erro ao adicionar navio.");
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

        private void NavioApagar_Click(object sender, EventArgs e)
        {
            if (listBoxNavios.SelectedItem == null)
            {
                MessageBox.Show("Selecione um Navio para apagar.");
                return;
            }

            string selectedLine = listBoxNavios.SelectedItem.ToString();

            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string id = parts[0].Trim();
            string nome = parts[1].Trim();

            DialogResult result = MessageBox.Show($"Tem a certeza que deseja apagar o navio {nome}?", "Confirmar Apagar", MessageBoxButtons.YesNo);
            if (result != DialogResult.Yes)
                return;

            SqlCommand cmd = new SqlCommand("DELETE FROM GP_Navio WHERE ID = @id;", cn);
            cmd.Parameters.AddWithValue("@id", id);

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show("Navio apagado com sucesso!");
                    LoadNavios();
                }
                else
                {
                    MessageBox.Show("Erro: Navio não encontrada.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao apagar: " + ex.Message);
            }
        }

        private void NavioEditar_Click(object sender, EventArgs e)
        {
            if (listBoxNavios.SelectedItem == null)
            {
                MessageBox.Show("Selecione uma empresa primeiro.");
                return;
            }

            string selectedLine = listBoxNavios.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Formato inesperado.");
                return;
            }

            string id = parts[0].Trim();
            string nome = NavioNome.Text;
            string capacidade = NavioCapacidade.Text;
            string nif = NavioEmpresaNIF.Text;

            SqlCommand cmd = new SqlCommand(
                "UPDATE GP_Navio SET Nome=@nome, Capacidade_Toneladas=@capacidade, NIF_Empresa=@nif WHERE ID=@id;", cn);

            cmd.Parameters.AddWithValue("@nome", nome);
            cmd.Parameters.AddWithValue("@capacidade", float.Parse(capacidade));
            cmd.Parameters.AddWithValue("@nif", nif);
            cmd.Parameters.AddWithValue("@id", int.Parse(id));

            try
            {
                int rows = cmd.ExecuteNonQuery();
                if (rows > 0)
                {
                    MessageBox.Show($"ID: {id}\nNome: {nome}\nCapacidade: {capacidade}\nNIF: {nif}");
                    MessageBox.Show("Navio atualizado com sucesso!");
                    LoadNavios();
                }
                else
                {
                    MessageBox.Show("Erro: Navio não encontrado.");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erro ao atualizar: " + ex.Message);
            }
        }

        private void ShowTrabalhadoresAssociados_Click(object sender, EventArgs e)
        {

        }

        private void listBoxNavios_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBoxNavios.SelectedItem == null)
                return;

            string selectedLine = listBoxNavios.SelectedItem.ToString();
            string[] parts = selectedLine.Split('|');
            if (parts.Length < 2)
            {
                MessageBox.Show("Erro ao analisar o Navio selecionado.");
                return;
            }

            string id = parts[0].Trim();
            string nome = parts[1].Trim();
            string capacidade = parts[2].Trim();
            string nif = parts[3].Trim();

            NavioNome.Text = nome;
            NavioCapacidade.Text = capacidade;
            NavioEmpresaNIF.Text = nif;
        }
    }
}
