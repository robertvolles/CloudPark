<template>
  <div>
    <!-- Formulário para cadastrar um novo veículo -->
    <form @submit.prevent="cadastrarVeiculo">
      <label>Marca:</label>
      <input v-model="novoVeiculo.make" required>

      <label>Modelo:</label>
      <input v-model="novoVeiculo.model" required>

      <!-- Outros campos do veículo (ano, cor, etc.) -->

      <button type="submit">Cadastrar</button>
    </form>

    <!-- Lista de veículos filtrados -->
    <div v-if="veiculos.length > 0">
      <h2>Veículos Encontrados:</h2>
      <ul>
        <li v-for="veiculo in veiculos" :key="veiculo.id">
          {{ veiculo.make }} - {{ veiculo.model }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      novoVeiculo: {
        make: '',
        model: '',
        // Outros campos do veículo
      },
      veiculos: [],
    };
  },
  methods: {
    cadastrarVeiculo() {
      // Enviar a solicitação POST para o endpoint de cadastro
      fetch('/api/vehicles', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.novoVeiculo),
      })
        .then(response => response.json())
        .then(data => {
          console.log('Veículo cadastrado com sucesso:', data);
          // Limpar o formulário após o cadastro, se necessário
          this.novoVeiculo = { make: '', model: '' };
        })
        .catch(error => {
          console.error('Erro ao cadastrar veículo:', error);
        });
    },

    consultarVeiculos() {
      // Enviar a solicitação GET para o endpoint de consulta com parâmetros de filtro
      fetch('/api/vehicles?make=Toyota&model=Camry')
        .then(response => response.json())
        .then(data => {
          this.veiculos = data;
        })
        .catch(error => {
          console.error('Erro ao consultar veículos:', error);
        });
    },
  },
  mounted() {
    // Chamar a função para consultar veículos quando o componente é montado
    this.consultarVeiculos();
  },
};
</script>