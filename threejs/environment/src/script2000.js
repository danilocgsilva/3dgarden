import './style.css'
import * as THREE from 'three'
import SceneBuilder from './building_environment/SceneBuilder'
import CreateTorus from './building_environment/CreateTorus'
import CreateCube from './building_environment/CreateCube'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import enableResize from './building_environment/enableResize'
import getVector from './building_environment/getVector'

const canvas = document.querySelector('canvas.webgl')
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}
const sceneBuilder = new SceneBuilder(sizes, canvas)

for (let i = 0; i <= 2000; i++) {
    sceneBuilder.setGeoCreator(new CreateCube(0.02, 0.02, 0.02))
    sceneBuilder.createGeo()
    const vetctor = getVector()
    sceneBuilder.exposeMesh().translateX(vetctor.x)
    sceneBuilder.exposeMesh().translateY(vetctor.y)
    sceneBuilder.exposeMesh().translateZ(vetctor.z)
}

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