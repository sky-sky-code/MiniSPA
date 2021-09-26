<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
.container{
    height: 100vh;
}

.single{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.single__item{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.form{
    width: 100%;
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
}

li:hover{
    color: #ffff;
    background-color: #0000;
}
</style>
