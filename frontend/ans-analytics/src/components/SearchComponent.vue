<template>
    <div class="container">
      <h1>Busca de Operadoras</h1>
      <div class="search-box">
        <input
          type="text"
          v-model="searchTerm"
          placeholder="Digite o nome da operadora..."
        />
        <button @click="fetchOperadoras">Pesquisar</button>
      </div>
      <table v-if="operadoras.length > 0">
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>CNPJ</th>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Modalidade</th>
            <th>Representante</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="operadora in operadoras" :key="operadora.Registro_ANS">
            <td>{{ operadora.Registro_ANS }}</td>
            <td>{{ operadora.CNPJ }}</td>
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.Nome_Fantasia }}</td>
            <td>{{ operadora.Modalidade }}</td>
            <td>{{ operadora.Representante }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Nenhuma operadora encontrada.</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        searchTerm: "",
        operadoras: [],
      };
    },
    methods: {
      async fetchOperadoras() {
        if (this.searchTerm.length > 1) {
          try {
            const response = await axios.get(
              `http://127.0.0.1:8000/operadoras?nome_fantasia=${this.searchTerm}`
            );
            this.operadoras = response.data;
          } catch (error) {
            console.error("Erro ao buscar operadoras:", error);
          }
        } else {
          this.operadoras = [];
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: 50px auto;
    padding: 20px;
    text-align: center;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    font-size: 24px;
    color: #333;
  }
  
  .search-box {
    margin-bottom: 20px;
  }
  
  .search-box input {
    width: 70%;
    padding: 10px;
    border: 2px solid #007BFF;
    border-radius: 5px;
    font-size: 16px;
    outline: none;
  }
  
  .search-box button {
    padding: 10px 15px;
    margin-left: 10px;
    border: none;
    background: #007BFF;
    color: #fff;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .search-box button:hover {
    background: #0056b3;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  table, th, td {
    border: 1px solid #dddddd;
  }
  
  th, td {
    padding: 8px 12px;
    text-align: left;
  }
  
  th {
    background-color: #f2f2f2;
  }
  
  p {
    color: #777;
    margin-top: 20px;
  }
  </style>
  