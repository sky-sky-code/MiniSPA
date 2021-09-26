<template>
<div class="container">
    <div class="single">
        <div class="single__item">
            <form class="form" @submit="onSubmit">
               <select class="form-select" id="select_column">
                  <option selected>Выбирите Колонку</option>
                  <option value="name_city">Город</option>
                  <option value="quantity_human">Количество человек</option>
                  <option value="distance">Растояние</option>
               </select>
               <select class="form-select" id="select_comparison">
                    <option selected>Выбирите Условие</option>
                    <option value=">">больше</option>
                    <option value="<">меньше</option>
                    <option value="=">равно</option>
                    <option value="содержит">Содержит</option>
               </select>
               <div class="input-group">
                  <input type="text" class="form-control" placeholder="Введите значение" id="data_input">
                  <button class="btn btn-outline-secondary" type="submit"
                      id="button-addon2" @click="clickBtnFilter()">Найти</button>
               </div>
            </form>
        </div>
        <div class="single__item">
            <table class="table table-dark table-striped">
                <thead>
                    <tr>
                        <th scope="col">Date</th>
                        <th scope="col">Name</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Distance</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="value in data_table">
                        <td>{{ value.data_departure }}</td>
                        <td>{{ value.name_city }}</td>
                        <td>{{ value.quantity_human }}</td>
                        <td>{{ value.distance }} км</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="single__item">
            <nav aria-label="...">
                <ul class="pagination">
                    <li class="page-item disabled">
                        <span class="page-link">Previous</span>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item" aria-current="page">
                        <span class="page-link">2</span>
                    </li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                        <a class="page-link" href="#">Next</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data_table: [],
      erorrs: [],
    };
  },
  methods: {
    getTable() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.data_table = res.data.singleTable;
        })
        .catch((error) => {
          // eslint-отключение следующей строки
          console.error(error);
        });
    },
    initFilter(){
      this.filterForm.column = '';
      this.filterForm.comparison = '';
      this.filterForm.data_input = '';
    },
    clickBtnFilter(){
      let column = document.getElementById('select_column').value;
      let comparison = document.getElementById('select_comparison').value;
      let data_input = document.getElementById('data_input').value;
      this.getFilter(column, comparison, data_input);
    },
    getFilter(column, comparison, data_input){
      const path =  `http://localhost:5000/${column}&${comparison}&${data_input}`
      axios.get(path)
      .then((res) => {
        this.data_table = res.data.filterData
      })
      .catch((error) => {
          console.error(error);
          this.getTable();
      })
    },
    onSubmit(evt){
      evt.preventDefault();
    },
  },
  created() {
    this.getTable();
  },
};
</script>
