import './style.css'
import * as THREE from 'three'
import SceneBuilder from './building_environment/SceneBuilder'
import CreateTorus from './building_environment/CreateTorus'
import CreateCube from './building_environment/CreateCube'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import enableResize from './building_environment/enableResize'

const canvas = document.querySelector('canvas.webgl')
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}
const sceneBuilder = new SceneBuilder(sizes, canvas)


for (let i = -2; i <= 2; i++) {
    sceneBuilder.setGeoCreator(new CreateCube())
    sceneBuilder.createGeo()
    sceneBuilder.exposeMesh().translateX(i / 2)
    sceneBuilder.exposeMesh().translateY(i / 2)
}

sceneBuilder.setGeoCreator(new CreateTorus())
sceneBuilder.createGeo()

const renderer = sceneBuilder.exposeRenderer()
const camera = sceneBuilder.exposeCamera()
const scene = sceneBuilder.exposeScene()

new OrbitControls(camera, renderer.domElement);

const tick = () => {
    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
}
tick()

enableResize(sizes, camera, renderer)