import './style.css'
import SceneBuilder from './building_environment/SceneBuilder'
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


// for (let i = -2; i <= 2; i++) {
sceneBuilder.setGeoCreator(new CreateCube())
sceneBuilder.createGeo()

// }

const renderer = sceneBuilder.exposeRenderer()
const camera = sceneBuilder.exposeCamera()
const scene = sceneBuilder.exposeScene()

new OrbitControls(camera, renderer.domElement);

const tick = () => {

    sceneBuilder.exposeMesh().translateX(0.0001)
    sceneBuilder.exposeMesh().translateY(0.0001)
    sceneBuilder.exposeMesh().translateZ(0.0001)
    
    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
}
tick()

enableResize(sizes, camera, renderer)