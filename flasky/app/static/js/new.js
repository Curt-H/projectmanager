let bindProjectClick = function () {
    let projectList = e('#id-project-list')
    projectList.addEventListener('click', function (t) {
        let target = t.target
        log(target)
        if (target.classList.contains('project-list')) {
            let project = target.innerHTML
            let formProject = e('#id-project')
            formProject.value = project
        } else {
            log('没点击到文本')
        }

    })
}

let bindDayAddClick = function () {
    let addBtn = e('#id-add-day')
    addBtn.addEventListener('click', function (t) {
        let day = e('#id-day')
        day.value = parseInt(day.value) + 1
    })

}
let bindDayDecClick = function () {
    let decBtn = e('#id-dec-day')
    decBtn.addEventListener('click', function (t) {
        let day = e('#id-day')
        day.value = parseInt(day.value) - 1
    })
}

let getDate = function () {
    let myDate = new Date()
    yy = myDate.getFullYear()
    mm = myDate.getMonth() + 1
    dd = myDate.getDate()

    let formYY = e('#id-year')
    let formMM = e('#id-month')
    let formDD = e('#id-day')

    formYY.value = yy
    formMM.value = mm
    formDD.value = dd
}


let __main = function () {
    getDate()
    bindProjectClick()
    bindDayAddClick()
    bindDayDecClick()
}


__main()