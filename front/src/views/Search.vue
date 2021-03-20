<template>
    <div class="GameCards">
        <GameCardsStack />
    </div>
</template>
<script>
import GameCardsStack from "../components/Card/GameCardsStack";

export default {
    name: "App",
    components: {
        GameCardsStack
    },

    data() {
        return {
        visibleCards: [
            {
                id: 1,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 2,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 3,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 4,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            }
        ]
        };
    },

    methods: {
        handleCardAccepted() {
            console.log("handleCardAccepted");
        },
        handleCardRejected() {
            console.log("handleCardRejected");
        },
        handleCardSkipped() {
            console.log("handleCardSkipped");
        },
        removeCardFromDeck() {
            this.visibleCards.shift();
        }
    }
};
</script>


<style lang="scss">
    #app {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        text-align: center;
    }
</style>