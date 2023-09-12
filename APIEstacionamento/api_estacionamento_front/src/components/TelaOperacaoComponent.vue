<template>
    <div>
      <h1>Tela de Operação</h1>
      
      <!-- Campo para inserir a placa do veículo -->
      <div>
        <label for="placa">Placa do Veículo:</label>
        <input type="text" id="placa" v-model="placa" disabled />
      </div>
      
      <!-- Campo para exibir o valor a cobrar -->
      <div>
        <label for="valor-a-cobrar">Valor a Cobrar:</label>
        <input type="text" id="valor-a-cobrar" :value="valorACobrar" disabled />
      </div>
      
      <!-- Grade de veículos no pátio -->
      <h2>Veículos no Pátio</h2>
      <table>
        <thead>
          <tr>
            <th>Data de Entrada</th>
            <th>Placa</th>
            <th>Cartão</th>
          </tr>
        </thead>
        <tbody>
          <!-- Iterar sobre a lista de veículos no pátio -->
          <tr v-for="(veiculo, index) in veiculos" :key="index">
            <td>{{ veiculo.dataEntrada }}</td>
            <td>{{ veiculo.placa }}</td>
            <td>{{ veiculo.cartao }}</td>
          </tr>
        </tbody>
      </table>
      
      <!-- Botões de entrada/saída -->
      <div>
        <button @click="registrarEntrada">Entrada</button>
        <button @click="registrarSaida">Saída</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        placa: '',
        valorACobrar: 0, // Inicialmente, o valor a cobrar é zero
        veiculos: [] // Suponha que esta seja uma lista de veículos no pátio
      };
    },
    methods: {
      registrarEntrada() {
        // Implemente a lógica para registrar a entrada do veículo
        // Isso pode incluir a adição de um veículo à lista 'veiculos'
      },
      registrarSaida() {
        // Implemente a lógica para registrar a saída do veículo
        // Isso pode incluir a remoção de um veículo da lista 'veiculos'
      }
    }
  };
  </script>