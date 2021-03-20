<template>
    <div>
        <div class="navBar">
            <div class="navItem">
                <b-icon
                    pack="fas"
                    icon="user"
                    size="is-small"
                />
            </div>
            <div class="navItem">
                <b-icon
                    pack="fas"
                    icon="user"
                    size="is-small"
                />
            </div>
        </div>
        <div>
            <router-view />
        </div>
    </div>
</template>

<style>
.icon.is-small {
    width: 40px;
    height: 40px;
}


.navBar {
    height: 50px;
    background: white;
    padding-top: 8px;
}

.navBar div {
    display: inline-block;
    width: 49%;
}

.navItem:hover {
    cursor: pointer;
}
</style>
